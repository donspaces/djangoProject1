onload = function()
{
    setInterval(go, 1000)
}

var time = 10;
function go()
{
    if(time > 0)
    {
        time--;
        document.getElementById("cd").innerText = time;
    }
    else
    {
        location.href = "/";
    }
}