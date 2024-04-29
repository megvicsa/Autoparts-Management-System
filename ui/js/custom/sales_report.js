$(document).ready(function() {
    $.get('http://127.0.0.1:3131/salesReport', function(response) {
        if(response) {
            var tableContent = '';

            $.each(response.top_selling_products, function(index, product) {
                tableContent += '<tr><td>' + product[0] + '</td><td>' + product[1] + '</td></tr>';
            });

            $.each(response.total_sales_per_day, function(index, sales) {
                tableContent += '<tr><td><b>Total Sales for ' + sales[0] + '</b></td><td>' + '$' + sales[1] + '</td></tr>';
            });

            var averageOrderValue = response.average_order_value[0].toFixed(2);
            tableContent += '<tr><td><b>Average Order Value</b></td><td>' + '$' + averageOrderValue + '</td></tr>';

            $("#ordersTable tbody").html(tableContent);
        }
    }).fail(function() {
        alert("Error fetching data.");
    });
});