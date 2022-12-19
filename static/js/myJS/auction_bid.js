// @ts-nocheck
document.addEventListener('DOMContentLoaded', function() {
    let url = "ws://" + window.location.host + "/ws/auction";
    let chatSocket = new ReconnectingWebSocket(url);
    
    chatSocket.onopen = function (event) {
        console.log("websocket connection opened!");
        fetchMessages();
    };
    chatSocket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log("message receive from server ...", data);
    }
    chatSocket.onclose = function (event) {
        console.error("websocket connection closed...");
    }

    function fetchMessages()
    {
        chatSocket.send(JSON.stringify({
            auction_id: 1,
            command: "fetch_messages"
        }));
    };
});