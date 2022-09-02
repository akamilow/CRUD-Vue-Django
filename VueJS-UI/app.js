const routes = [
    {path: '/alimentosview', component: alimentosview},
    {path: '/cocinaview', component: cocinaview},
    {path: '/limpiezaview', component: limpiezaview},
    {path: '/proveedoresview', component: proveedoresview},
    {path: '/informacion', component: informacion}
]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})
  
const app = Vue.createApp({})

app.use(router)
  
app.mount('#app')