// "Корзина"
$(function () {
  // localStorage.clear();
  function totalQuantity() {
    // Відображення загальної кількості товару в корзині на сайті.
    let $ProductInBasket = $('.products-in-basket');
    let sum_quantity = 0;

    let value = localStorage.getItem('Cart');
    let Cart = JSON.parse(value);

    $.each(Cart, function (product) {
      sum_quantity += +Cart[product].quantity;
    })

    $ProductInBasket.text(sum_quantity);
  }
  totalQuantity();

  (function modalCart() {
    // Форма добавлення товару в корзину.

    $('.btn-cart').click(function modalDataRender() {
      // Заповнення модальної форми, добавлення товару в корзину.
      $('.modal-dialog-delete').hide();
      $('.modal-dialog-add').show();
      let str_product_data = $(this).attr('product_data');
      let product_data = JSON.parse(str_product_data);

      $('.modal_product_img').attr('src', product_data.image);
      $('.modal-product-name').text(product_data.name);
      $('.modal_product_price').text(product_data.price + " " + '₴');
      $('#addCart').attr('modal_product_id', product_data.id);
      $('#addCart').attr('modal_product_data', str_product_data);

      let str_Cart = localStorage.getItem('Cart')
      Cart = JSON.parse(str_Cart)

      if (product_data.id in Cart) {
        $quantityNum.val(Cart[product_data.id].quantity);
      } else {
        $quantityNum.val(1);
        addItem();
      }

      price = +product_data.price;
      quantity = +$quantityNum.val();
      modalTotalPrice();
    })

    let $quantityNum = $(".quantity-num");

    function modalTotalPrice() {
      let price = $('.modal_product_price').text().replace('₴', '');
      let quantity = $quantityNum.val();
      let total_price = (price * quantity).toFixed(2);
      $('#total_price').text(total_price + " " + '₴');
    }

    function addItem() {
      // Додати товар в корзину.
      let id = $('#addCart').attr('modal_product_id');

      let product_data = JSON.parse($('#addCart').attr('modal_product_data'));
      let quantity = $quantityNum.val();
      delete product_data.id
      product_data.quantity = quantity;
      let Cart

      if (localStorage.getItem('Cart') !== null) {
        let str_Cart = localStorage.getItem('Cart');
        Cart = JSON.parse(str_Cart)
        Cart[id] = product_data;
      } else {
        Cart = Object.create({});
        Cart[id] = product_data;
      }

      if (quantity > 0) {
        localStorage.setItem('Cart', JSON.stringify(Cart));
        totalQuantity();
      }
    }

    function deleteItem() {
      // Видалити товар з корзини.
      let id = $('#addCart').attr('modal_product_id');
      let str_Cart = localStorage.getItem('Cart');
      let Cart = JSON.parse(str_Cart);
      delete Cart[id]
      localStorage.setItem('Cart', JSON.stringify(Cart));
      totalQuantity();
    }

    $(".quantity-item-plus").click(function quantityPlus() {
      //Кнопка: Збільшити кількість товару на 1.
      $quantityNum.val(+$quantityNum.val() + 1);
      addItem();
      modalTotalPrice();
    })

    $(".quantity-item-minus").click(function quantityMinus() {
      //Кнопка: Зменшити кількість товару на 1.
      if ($quantityNum.val() > 1) {
        $quantityNum.val(+$quantityNum.val() - 1);
        addItem();
        modalTotalPrice();
      }
    })

    $(".quantity-item-delete").click(function modalDelete() {
      //Кнопка: видалити товар з корзини.
      deleteItem();
      $('.modal-dialog-add').hide();
      $('.modal-dialog-delete').show();
    })
  })();


  // order_checkout cart

  (function renderCheckoutCart() {
    let $CheckoutCart = $('.checkout-cart > .card-body');
    let $totalPrice = $('.total-price');
    let total_price = 0;

    let value = localStorage.getItem('Cart');
    let Cart = JSON.parse(value);
    $.each(Cart, function (product) {
      $CheckoutCart.append(
        '<div class="row align-items-center cart-item">' +
        '<div class="col h6">' + Cart[product].name + '</div>' +
        '<div class="col-2 px-0"><img src="' + Cart[product].image + '" class="card-img" alt=""></div>' +
        '<div class="col-3">' + Cart[product].price + '₴</div>' +
        '<div class="col-1 px-0">' + Cart[product].quantity + '</div>' +
        '</div>'
      );
      total_price = total_price + (Cart[product].price * Cart[product].quantity);
    })

    $totalPrice.text('Загальна вартість: ' + total_price.toFixed(2) + '₴');
  })();

  // Передача даних корзини в форму перед відправкою на сервер.
  $('#checkout-form').submit(function (e) {
    e.preventDefault();
    let form_data = $(this).serialize();
    console.log(form_data);
    let Cart = JSON.parse(localStorage.getItem('Cart'));
    for (let product in Cart) {
      Cart[product] = Cart[product].quantity
    }
    console.log(form_data + '&Cart=' + JSON.stringify(Cart));
    $.ajax({
      type: "POST",
      url: "/order/checkout/",
      data: form_data + '&Cart=' + JSON.stringify(Cart),
      success: function (response) {
        alert(response)
        window.location = "http://127.0.0.1:8000/products/";
      }
    });
  });
});


// Випадаюче меню "Категорії"
$(document).on('click', '.dropdown-menu', function (e) {
  e.stopPropagation();
});

// clickable on mobile view
if ($(window).width() < 992) {
  $('.has-submenu a').click(function (e) {
    e.preventDefault();
    $(this).next('.megasubmenu').toggle();

    $('.dropdown').on('hide.bs.dropdown', function () {
      $(this).find('.megasubmenu').hide();
    })
  });
}