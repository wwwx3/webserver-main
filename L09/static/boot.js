// Clear Pyscript console when the page loads 

(function (){
    const method = ["log", "debug" , "warn","info","error"];
    const original = {};

    method.forEach(m => original[m] = console[m]);

    function ignore(args) {
        const txt = args?.[0]?.toString?.() || "";

        return (
            txt.includes("[pyscript") ||
            txt.includes("[py-script") ||
            txt.includes("[py-terminal") ||
            txt.includes("[py-splashscreen") ||
            txt.includes("Python initialization complete") ||
            txt.includes("[pyscript/") 
        )
    }

    method.forEach(method => {
        console[method] = (...args) => {
            if (!ignore(args)) {
                original[method](...args);
            }
        };
    });
    
})();