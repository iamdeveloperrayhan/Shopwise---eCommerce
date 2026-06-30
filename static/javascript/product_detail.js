$(document).ready(function() {
    $('.xzoom-gallery').on('click', function(e) {
    e.preventDefault();
    var newSrc = $(this).attr('xpreview') || $(this).attr('src');
    var newOriginal = $(this).closest('a').attr('href') || newSrc;
    var mainImage = $('.xzoom').first();
    if (mainImage.length) {
        mainImage.attr('src', newSrc);
        mainImage.attr('xoriginal', newOriginal);
    }
    });

    // Star Rating System - Add Review
    let selectedRating = 0;
    
    $('.star-rating').on('click', function() {
    selectedRating = $(this).data('value');
    $('#id_rating').val(selectedRating);
    updateStars(selectedRating);
    });

    $('.star-rating').on('mouseover', function() {
    let hoverRating = $(this).data('value');
    updateStars(hoverRating);
    });

    $('.rating-stars').on('mouseout', function() {
    updateStars(selectedRating);
    });

    function updateStars(rating) {
    $('.star-rating').each(function() {
        if ($(this).data('value') <= rating) {
        $(this).removeClass('fa-regular').addClass('fa-solid').css('color', 'gold');
        } else {
        $(this).removeClass('fa-solid').addClass('fa-regular').css('color', 'gold');
        }
    }); 
    }
});

// Edit Review Stars Handler
function initEditStars(reviewId, currentRating) {
    let selectedEditRating = currentRating;
    const container = $(`#editReviewModal${reviewId}`);
    
    container.find('.star-rating-edit').on('click', function() {
    selectedEditRating = $(this).data('value');
    $(`#edit_rating_${reviewId}`).val(selectedEditRating);
    updateEditStars(reviewId, selectedEditRating);
    });

    container.find('.star-rating-edit').on('mouseover', function() {
    let hoverRating = $(this).data('value');
    updateEditStars(reviewId, hoverRating);
    });

    container.find(`#edit_stars_${reviewId}`).on('mouseout', function() {
    updateEditStars(reviewId, selectedEditRating);
    });

    // Initialize stars display
    updateEditStars(reviewId, currentRating);
}

function updateEditStars(reviewId, rating) {
    $(`#editReviewModal${reviewId}`).find('.star-rating-edit').each(function() {
    if ($(this).data('value') <= rating) {
        $(this).removeClass('fa-regular').addClass('fa-solid').css('color', 'gold');
    } else {
        $(this).removeClass('fa-solid').addClass('fa-regular').css('color', 'gold');
    }
    });
}
function searchToggle(obj, evt){
var container = $(obj).closest('.search-wrapper');
    if(!container.hasClass('active')){
        container.addClass('active');
        evt.preventDefault();
    }
    else if(container.hasClass('active') && $(obj).closest('.input-holder').length == 0){
        container.removeClass('active');
        container.find('.search-input').val('');
    }
}
