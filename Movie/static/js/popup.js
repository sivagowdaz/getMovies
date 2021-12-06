function toggle(type) {
    let req_div;
    if (type === 'toggle_other_movie') {
        req_div = document.querySelector('.other_movie')
    }
    else if (type === 'toggle_genre') {
        req_div = document.querySelector('.genreform')
    }

    if (req_div.style.display === 'none') {
        req_div.style.display = 'flex'
    } else {
        req_div.style.display = 'none'
    }
}

function scroll_top() {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    })
}

function scroll_left() {
    document.querySelector('.recent_movie_list').scrollLeft += 400
}

function scroll_right() {
    document.querySelector('.recent_movie_list').scrollLeft -= 400
}