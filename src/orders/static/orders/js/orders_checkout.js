function getCities(container) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "https://api.novaposhta.ua/v2.0/json/",
        "method": "POST",
        "headers": {
            "content-type": "application/json",
        },
        "processData": false,
        "data": JSON.stringify({
            "modelName": "AddressGeneral",
            "calledMethod": "getCities",
            "Warehouse": "1",
        })
    }

    $.ajax(settings).done(function (response) {
        console.log(response);
        for (let city in response.data) {
            container.append(
                '<option>' + response.data[city].Description + '</option>'
            )
        };
    });
}

function getWarehouses(container, city) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "https://api.novaposhta.ua/v2.0/json/",
        "method": "POST",
        "headers": {
            "content-type": "application/json",
        },
        "processData": false,
        "data": JSON.stringify({
            "modelName": "AddressGeneral",
            "calledMethod": "getWarehouses",
            "methodProperties": {
                "CityName": city,
                "Language": "ua"
            }
        })
    }

    $.ajax(settings).done(function (response) {
        console.log(response);
        for (let office in response.data) {
            container.append(
                '<option>' + response.data[office].Description + '</option>'
            )
        };
    });
}

function matchStart(params, data) {

    if ($.trim(params.term) === '') {
        return data;
    }
    
    if (typeof data.text === 'undefined') {
        return null;
    }
    
    if (data.text.indexOf(params.term) === 0) {
        var modifiedData = $.extend({}, data, true);
        return modifiedData;
    }

    return null;
}


$(document).ready(function CheckoutMain() {

    let $CityContainer = $(".nova-poshta-city");
    let $WarehousesContainer = $(".nova-poshta-warehouses");
    let $AddComment = $('.add-comment');

    getCities($CityContainer);

    $WarehousesContainer.select2({
        width: '100%',
        placeholder: "Оберіть відділення",
    });

    $CityContainer.select2({
        width: '100%',
        placeholder: "Оберіть місто",
        matcher: matchStart
    });

    $CityContainer.change(function(){
        $WarehousesContainer.parent().hide(300);

        let selected_city = $('#select2-selectCity-container').text();
        $WarehousesContainer.children('option').remove();
        getWarehouses($WarehousesContainer, selected_city);

        $WarehousesContainer.parent().show(300);
    });

    $AddComment.click(function(){
        let $CommentInput = $('.comment-input');
        $CommentInput.slideToggle(300,"linear");
    });
});