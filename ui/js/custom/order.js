var productPrices = {};

$(function () {
    //Json data by api call for order table
    $.get(productListApiUrl, function (response) {
        productPrices = {}
        if(response) {
            var options = '<option value="">--Select--</option>';
            $.each(response, function(index, product) {
                options += '<option value="'+ product.product_id +'">'+ product.name +'</option>';
                productPrices[product.product_id] = product.price;
            });
            $(".product-box").find("select").empty().html(options);
        }
    });
});

$("#addMoreButton").click(function () {
    var row = $(".product-box").html();
    $(".product-box-extra").append(row);
    $(".product-box-extra .remove-row").last().removeClass('hideit');
    $(".product-box-extra .product-price").last().text('0.0');
    $(".product-box-extra .product-qty").last().val('1');
    $(".product-box-extra .product-total").last().text('0.0');
});

$(document).on("click", ".remove-row", function (){
    $(this).closest('.row').remove();
    calculateValue();
});

$(document).on("change", ".cart-product", function (){
    var product_id = $(this).val();
    var price = productPrices[product_id];

    $(this).closest('.row').find('#product_price').val(price);
    calculateValue();
});

$(document).on("change", ".product-qty", function (e){
    calculateValue();
});


$("#saveOrder").on("click", function() {
    var formData = $("form").serializeArray();
    var request_load = {
        customer_name: null,
        total_price: 0,
        order_details: []
    };
    
    for (var i = 0; i < formData.length; ++i) {
        var element = formData[i];

        switch (element.name) {
            case 'customerName':
                request_load.customer_name = element.value;
                break;
            case 'product_total_price':
                request_load.total_price += parseFloat(element.value);
                break;
            case 'product':
                request_load.order_details.push({
                    product_id: parseInt(element.value), 
                    quatity: 0, 
                    total_price: 0 
                });
                break;
            case 'qty':
                request_load.order_details[request_load.order_details.length - 1].quatity = parseInt(element.value);
                break;
            case 'item_total':
                request_load.order_details[request_load.order_details.length - 1].total_price = parseFloat(element.value);
                break;
        }
    }
    
    callApi("POST", orderSaveApiUrl, {
        'data': JSON.stringify(request_load)
    });
});
