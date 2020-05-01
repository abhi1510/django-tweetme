const tweetsContainerEl = $('#tweetsContainer');

const getTweetHtmlStr = (authorImg, author, content, timestamp) => {
    return `<div class="card-body" style="border-bottom: 1px solid rgba(0,0,0,0.125)">
        <div class="media tweet">
            <img src="${authorImg}" class="mr-3 profile-img" alt="profile-image">
            <div class="media-body">
                <h6 class="title">
                    @${author}
                    <span class="ml-2 lead" style="font-size: 0.7rem">${timestamp} ago</span>    
                </h6>
                <div class="text">${content}</div>
                <div class="meta">
                    <span class="mr-4">
                        <i class="fa fa-comment-o"></i> 3.5K
                    </span>
                    <span class="mr-4">
                        <i class="fa fa-heart-o"></i> 10.8K
                    </span>
                </div>
            </div>
        </div>
    </div>`
}

const loadTweets = () => {
    $.ajax({
        type: 'GET',
        url: '/api/tweets/',
        dataType: 'json',
        success: function(response){
            tweetsContainerEl.empty();
            response.forEach((tweet) => {
                let author = tweet.author_details;
                let tweetsStr = getTweetHtmlStr(author.avatar, author.username, tweet.content, tweet.timestamp);
                tweetsContainerEl.append(tweetsStr);
            })
        }
    })
}

$('#tweetForm').submit((e) => {
    e.preventDefault();
    let authorEl = $("#tweetForm :input[name='author']");
    let contentEl = $("#tweetForm :input[name='content']");
    let csrfEl = $("#tweetForm :input[name='csrf']");
    let data = {
        "content": contentEl.val(),
        "author": parseInt(authorEl.val()),
        "csrfmiddlewaretoken": csrfEl.val()
    }
    $.ajax({
        type: 'POST',
        url: '/api/tweets/',
        data: data,
        dataType: 'json',
        success: function(response){
            e.target.reset();
            loadTweets();
        }
    });
});

setTimeout(() => {
    loadTweets();
}, 2000)

let notificationsCount = 0;
let notificationsHolderEl = $("[aria-labelledby='notificationDropdown']")

const pushNotification = (text) => {
    notificationsCount += 1;
    $('.notification-label').text(notificationsCount);
    notificationsHolderEl.append(`<div class="dropdown-item">${text}</div>`);
}

var source = new EventSource("/notifications");
source.onmessage = function(event) {
    let msg = event.data;
    pushNotification(msg);
    console.log('Received: ', msg);
};