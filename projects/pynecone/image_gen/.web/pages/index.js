import {Fragment, useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Button, Center, CircularProgress, Divider, Heading, Image, Input, VStack} from "@chakra-ui/react"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"image_made": false, "image_processing": false, "image_url": "", "prompt": "", "events": [{"name": "state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT)
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<Center sx={{"width": "100%", "height": "100vh", "background": "radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .20), hsla(0, 0%, 100%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .18), hsla(0, 0%, 100%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .28), hsla(0, 0%, 100%, 0) 55%)"}}><VStack sx={{"bg": "white", "padding": "2em", "shadow": "1g", "borderRadius": "1g"}}><Heading sx={{"fontSize": "1.5em"}}>{`DALL-E`}</Heading>
<Input placeholder="Enter a prompt.."
type="text"
onBlur={(_e) => Event([E("state.set_prompt", {value:_e.target.value})])}/>
<Button onClick={() => Event([E("state.process_image", {}),E("state.get_image", {})])}
sx={{"width": "100%"}}>{`Generate Image`}</Button>
<Divider/>
{state.image_processing ? <CircularProgress isIndeterminate={true}/> : state.image_made ? <Image src={state.image_url}
sx={{"height": "25em", "width": "25em"}}/> : <Fragment/>}</VStack>
<NextHead><title>{`Pynecone: DALL-E`}</title>
<meta name="description"
content="A Pynecone app."/>
<meta property="og:image"
content="favicon.ico"/></NextHead></Center>
)
}