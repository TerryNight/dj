window.onload = function(){
    $('.basket_list').on(types:'click', selector: 'input[type="number"]', data:function(){
    var target_href = event.taget;
    if(target_href){
        &.ajax(urls:{
            url:"/basket/edit/"+target_href.name + "/" +target_href.value + "/",
            success: function (data) {
                    $('.basket_list').html(data.result);
                    console.lig('ajax done')
                },
            })
        }
     });
    }