const firebaseApp = firebase.initializeApp({
    apiKey: "AIzaSyCBMG0keFf8AsPcnavM-aD0Wm__o5YWAiU",
    authDomain: "c3coding-4fac8.firebaseapp.com",
    databaseURL: "https://c3coding-4fac8-default-rtdb.firebaseio.com",
    projectId: "c3coding-4fac8",
    storageBucket: "c3coding-4fac8.appspot.com",
    messagingSenderId: "692798403137",
    appId: "1:692798403137:web:0d726281ca29e0245a8cc0"
});

const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

const register = () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('pwd').value;
    // console.log(email, password);

    auth.createUserWithEmailAndPassword(email, password)
    .then((res) => {
        console.log(res.user);
    })
    .catch((error) => {
        alert(error.message)
        console.log(error.code);
        console.log(error.message);
    })
}

const login = () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('pwd').value;

    auth.signInWithEmailAndPassword(email, password)
    .then((res) => {
        console.log(res.user);
    })
    .catch((err) => {
        alert(err.message);
        console.log(err.code);
        console.log(err.message);
    })
}

const saveData = () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('pwd').value;

    db.collection('users')
    .add({
        email: email,
        password: password
    })
    .then((docRef) => {
        console.log("Document written with ID: ", docRef.id);
    })
    .catch((error) => {
        console.error("Error adding document: ", error);
    })
}

const readData = () => {
    db.collection('users')
    .get()
    .then((data) => {
        console.log(data.docs.map((item) => {
            return {...item.data(), id: item.id}
        }))
    })
}

const updateData = () => {
    db.collection('users').doc("My571pOJrDxUv6gJnivs")
    .update({
        email: 'c3coding@creverse.com',
        password: 'creverse12!!'
    })
    .then((res) => {
        alert("Data Updated")
    })
    .catch((error) => {
        alert(error.message)
    })
}

const deleteData = () => {
    db.collection('users').doc("My571pOJrDxUv6gJnivs").delete()
    .then((res) => {
        alert("Data Deleted")
    })
    .catch((error) => {
        alert(error.message)
    })
}