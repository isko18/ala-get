(function () {

    'use strict';

    const mySwiper = new Swiper('.swiper-container', {

        loop: true,

        slidesPerView: 'auto',
        centeredSlides: false,

        a11y: false,
        keyboardControl: true,
        grabCursor: true,

        // pagination
        pagination: '.swiper-pagination',
        paginationClickable: true,

        // navigation arrows
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev'
    });





})(); /* IIFE end */