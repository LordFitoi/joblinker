<template>
    <div>
        <h1>Atlassian</h1>
        <div>
            <div class="description">
                <p>
                    About Atlassian
                    The Future of Atlassian starts with you.
        
                    At Atlassian, our future is rooted in helping teams unleash their potential by building tools that inspire collaboration and facilitate growth — interested in what’s next? We’re looking for people who believe that we can accomplish so much more together than apart.
        
                    Let’s build our future, together
                    We’ve got an ambitious road ahead. Join our team and help us shape the future.
        
                    Going virtual together
                    We're entering a new era of work, one that will see more of our day-to-day tasks taking place in a virtual environment, and we're adapting to embrace this change.
        
                    Into the cloud
                    Our products help teams of all sizes to do amazing things. As we bring our product suite to the cloud we're innovating every day.
        
                    Atlassian is for everyone
                    It's our mission to unleash the potential in every team, and we know that teams perform best when they are diverse and every team member feels that they belong. It's the unique contributions of all Atlassians that drive our success, and we're committed to building a culture where everyone has the opportunity to do meaningful work and be recognized for their efforts. To that end, we are committed to providing an environment free of discrimination for everyone.
                </p>
            </div>
            <div class="container">
                <PlaceholderJobpost v-for="_ in 10" :key="_"></PlaceholderJobpost>
    
                <div class="table--footer">
                    <div class="button--secondary">Previous</div>
                    <p class="page-counter">
                        Page 1 of 1
                    </p>
                    <div class="button--secondary ml-auto">Next</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
definePageMeta({ layout: "content" });
</script>