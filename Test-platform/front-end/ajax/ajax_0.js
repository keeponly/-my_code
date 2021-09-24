$(function(){
    //ajax请求
    $('#login_in').click(function(){

    //获取账号
        var user = $('#username').val();
        //获取密码
        var pwd = $('#pwd').val();
        //相关加密处理
    //发送ajax请求
    $.ajax({
    url:'/login',
    data:{'user':user,'pwd':pwd},
    method:'POST',
    dataType:'json',
        success:function(data){
        if(data.code == '1'){
            alert(data.msg)}
        else{
            alert(data.msg)
            }
        }
    })
    });
})