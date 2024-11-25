
$.ajax({
    type: "GET",
    url: "/compare/",
    success: function(response){
        // console.log(response.data)
        const data = response.data
        data.map(profile=>{
            console.log(profile.id)
        })
    },
    error: function(error){
        console.log(error)
    }
})