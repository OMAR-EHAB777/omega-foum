$(function () {
      // custom formatting example
      "use strict";
      $('.timer').countTo({
        speed:10000
      });

});
 $('.dropdown').hover(function () {
          $(this)('ul').slideToggle(400)

      });
$(document).ready(function(){
  $(".carouselExampleIndicators").carousel({
      interval: 2000
  });
});
$(document).ready(function(){
    $('.customer-logos').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });
});



