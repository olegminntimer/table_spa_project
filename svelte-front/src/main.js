import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'

// axios.defaults.baseURL = 'http://localhost:8000/api/items/'

const app = mount(App, {
  target: document.getElementById('app'),
})

// const app = new App({
//   target: document.getElementById('app')
// });

export default app
