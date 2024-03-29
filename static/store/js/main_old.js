function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
function addCart(idProduct){
        console.log(idProduct)

        fetch('/addCart/'+idProduct,{
            method: 'POST',
            headers:{
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken,
            }
        }
        )
        .then(response => {
                return response.json() //Convert response to JSON
        })
        .then(data => {
            var number_products = document.getElementById("number_products");
            json1 = data.json1
            json2 = JSON.parse(data.json2)
            var image_url_product = json2[0].image_url;
            var name_product = json2[0].name;
            number_products.textContent = json1
            console.log(name_product)
            console.log(image_url_product)
            showModal(name_product, image_url_product)
        });
    };
function addCartProductDetail(idProduct){
        console.log(idProduct)

        fetch('../addCart/'+idProduct,{
            method: 'POST',
            headers:{
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken,
            }
        }
        )
        .then(response => {
                return response.json() //Convert response to JSON
        })
        .then(data => {
            var number_products = document.getElementById("number_products");
            json1 = data.json1
            json2 = JSON.parse(data.json2)
            var image_url_product = json2[0].image_url;
            var name_product = json2[0].name;
            number_products.textContent = json1
            console.log(name_product)
            console.log(image_url_product)
            showModal(name_product, image_url_product)
        });
    };


function showModal(name_product, image_url_product) {
      var modalContent = document.getElementsByClassName("modal-body");
        console.log(name_product)
        console.log(image_url_product)

        const img = modalContent[0].querySelector("img");
        const paragraph = modalContent[0].querySelector("p");
        console.log(img)
        img.src = image_url_product;
        paragraph.textContent = name_product

        $('#modalBoot').modal('show');
                setTimeout(function() {
                    $('#modalBoot').modal('hide');
                  }, 2100);

    }

(function ($) {
    "use strict";

    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });
    


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

    // Product Quantity

    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;

        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
        createJSON()
        //total_price();
    });

    function createJSON() {
      const myTable = document.getElementById("CartTable");
      const rows = myTable.getElementsByTagName("tr");
      const data = [];

      // Recorrer cada fila de la tabla (empezar en la segunda fila para ignorar la fila de encabezado)
      for (let i = 1; i < rows.length; i++) {
        const row = rows[i].getElementsByTagName("td");

        // Obtener los valores de las celdas y construir un objeto JavaScript
        const jsonRow = {
          id: row[0].textContent,
            quantity: parseInt(row[4].querySelector('input').value)
        };


        // Agregar el objeto a la lista de datos
        data.push(jsonRow);
      }
      // Convertir el objeto JavaScript en una cadena JSON
      const json = JSON.stringify(data);

      fetch('updateCart',{
            method: 'POST',
          body: json,
            headers:{
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken,
            }
        }
        )
        .then(response => {
                return response.json() //Convert response to JSON
        })
        .then(data => {
                var subTotal = document.getElementById("subtotal");
                var totalPrice = document.getElementById("total_price");
                var subTotalcount = 0;

                for (let i = 0; i < data.length; i++) {
                    var totalElement = document.getElementById("total_price_"+data[i]["id"]);
                    totalElement.textContent = "$"+data[i]["total"]
                    subTotalcount += data[i]["total"]
                }
                subTotal.textContent = "$"+subTotalcount
                totalPrice.textContent = "$"+(subTotalcount+15000)
        });



    }



    //Data table
    $(document).ready(function() {
        $('#table-data-model').DataTable({
            responsive: true
        });
        
    });

})(jQuery);