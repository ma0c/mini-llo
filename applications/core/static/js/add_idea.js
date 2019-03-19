$(document).ready(function()
{
    var clear_and_hide_modal = function () {
        $("#idea").modal("hide");
        $("#idea_idea").val("");
    };

    $("#send_idea").click(function (event) {
            var board_id = $("#idea_board").val();
            var idea_text = $("#idea_idea").val();
            var request = new Request(
                '{{ create_idea_api_url }}',
                {
                    method: "POST",
                    body: JSON.stringify({
                        "board": board_id,
                        "text": idea_text
                    }),
                    headers: {
                        "Authorization": "Token {{ user.auth_token }}",
                        "Content-Type": "application/json"
                    }
                }
            );

            fetch(request)
                .then(response => {
                    console.log(response);
                    if (response.status === 201) {
                        return response.json();
                    } else {
                        throw new Error("Bad response from server")
                    }
                })
                .then(
                    json_response => {
                        if (json_response["is_approved"]) {
                            $(`#board_idea_${json_response["board_id"]}`).append(`<li>${json_response["text"]} </li>`)
                        } else {
                            $.snackbar({content: "{% trans 'Idea submitted and needs to be approved by board owner' %}"});
                        }

                        clear_and_hide_modal();
                    }
                ).catch(
                error => {
                    $.snackbar({content: error});
                    clear_and_hide_modal();
                }
            );
        }
    );
});