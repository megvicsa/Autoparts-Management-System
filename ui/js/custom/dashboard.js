$(function () {
    $.get(orderListApiUrl, function (response) {
        if(response) {
            var table = '';
            var totalCost = 0;
            $.each(response, function(index, order) {
                totalCost += parseFloat(order.total_price);
                table += '<tr>' +
                    '<td>'+ order.date +'</td>'+
                    '<td>'+ order.order_id +'</td>'+
                    '<td>'+ order.customer_name +'</td>'+
                    '<td>'+ order.total_price +' USD</td></tr>';
            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+ totalCost +' USD</b></td></tr>';
            $("table").find('tbody').empty().html(table);
        }
    });
});