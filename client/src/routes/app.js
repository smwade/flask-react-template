import Dashboard from 'views/Main/Main';

const appRoutes = [
    { path: "/main", name: "Main", icon: "pe-7s-graph", component: Dashboard },
    { redirect: true, path:"/", to:"/main", name: "Main" }
];

export default appRoutes;
