if (process.argv[2] === "child") {
    console.log("process on child", process.pid);
} else {
    const fork = require("child_process").fork;
    const controller = new AbortController();
    const { signal } = controller;

    const child = fork(__filename,["child"],{ signal });
    child.on("error",err => {
        console.log("main process error:", err)
    });
    console.log("process on main", process.pid);
    // controller.abort();
}