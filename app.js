$(function(){

    $('#connect').on('click',()=>{
        var ws = new WebSocket("ws://192.168.1.4:10005/");
        ws.onmessage = function(message){
            console.log(message.data)
        }
        setTimeout(function(){
            ws.send('COM:'+$('#roomid').val());
        }, 6000)
    })

})
