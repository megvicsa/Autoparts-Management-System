var productModal = $("#productModal");

    $(function () {
        $.get(productListApiUrl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index, product) {
                    table += '<tr data-id="'+ product.product_id +'" data-name="'+ product.name +'" data-brand="'+ product.brand_id +'" data-price="'+ product.price +'">' +
                        '<td>'+ product.name +'</td>'+
                        '<td>'+ product.brand_name +'</td>'+
                        '<td>'+ product.price +'</td>'+
                        '<td><span class="btn btn-xs btn-primary edit-product">Edit</span> <span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });

    $(document).on("click", ".delete-product", function (){
        var tr = $(this).closest('tr');
        var data = {
            product_id : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?");
        if (isDelete) {
            callApi("POST", productDeleteApiUrl, data);
        }
    });

    $("#saveProduct").on("click", function () {
        var formData = $("#productForm").serializeArray();
        var requestPayload = {
            product_id: null, 
            product_name: null,
            brand_id: null,
            price: null
        };
    
        formData.forEach(function(element) {
            if (element.name === 'product_id' && element.value) {
                requestPayload.product_id = element.value;
            } else if (element.name === 'name') {
                requestPayload.product_name = element.value;
            } else if (element.name === 'brand') {
                requestPayload.brand_id = element.value;
            } else if (element.name === 'price') {
                requestPayload.price = element.value;
            }
        });

        callApi("POST", productSaveApiUrl, { 'data': JSON.stringify(requestPayload) });
        
    });

    productModal.on('hide.bs.modal', function(){
        $("#id").val('0');
        $("#name, #brand, #price").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    productModal.on('show.bs.modal', function(){
        $.get(brandListApiUrl, function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, brand) {
                    options += '<option value="'+ brand.brand_id +'">'+ brand.name +'</option>';
                });
                $("#brand").empty().html(options);
            }
        });
    });

    function showEditModal(productId, productName, brandId, price) {
        $("#editName").val(productName);
        $("#editPrice").val(price);
        $("#editModal").data('product-id', productId);

        $("#editModal").css("display", "block");

        populateBrandDropdown(brandId);
    }

function closeEditModal() {
    $("#editModal").css("display", "none");
}

$(document).on("click", ".edit-product", function () {
    var tr = $(this).closest('tr');
    var productId = tr.data('id');
    var productName = tr.data('name');
    var brandId = tr.data('brand');
    var price = tr.data('price');

    showEditModal(productId, productName, brandId, price);
});


function populateBrandDropdown(selectedBrandId) {
    $.get(brandListApiUrl, function (response) {
        var options = '<option value="">--Select--</option>';
        $.each(response, function(index, brand) {
            options += `<option value="${brand.brand_id}" ${(brand.brand_id == selectedBrandId ? 'selected' : '')}>${brand.name}</option>`;
        });
        $("#editBrand").html(options);
    });
}

$("#updateProduct").on("click", function () {
    var productId = $("#editModal").data('product-id');
    var updatedName = $("#editName").val();
    var updatedBrandId = $("#editBrand").val();
    var updatedPrice = $("#editPrice").val();

    var data = {
        product_name: updatedName,
        brand_id: updatedBrandId,
        price: updatedPrice
    };

    $.ajax({
        url: `http://127.0.0.1:3131/updateProduct/${productId}`,
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (result) {
            console.log("Product Updated: ", result);
            closeEditModal();
        },
        error: function (request, status, error) {
            console.log("Error updating product: ", request.responseText);
        }
    });
});


$(document).on("click", ".close-button", function () {
    closeEditModal();
});
