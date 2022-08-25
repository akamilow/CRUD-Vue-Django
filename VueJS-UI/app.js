const routes = [
    {path: '/productoview', component: productoview},
    {path: '/about', component: about},
]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})
  
const app = Vue.createApp({})

app.use(router)
  
app.mount('#app')