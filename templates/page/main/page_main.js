document.addEventListener('DOMContentLoaded', () => {
    const you = "Chris", name = "Charles", surname = "Barkley"
    const tmp = `<p>Hello, ${you}. My name is ${name} ${surname}</p>`
    const el = document.querySelector("body")
    el.insertAdjacentHTML('beforeend', tmp)
    console.log('hello wodddddssr')
});