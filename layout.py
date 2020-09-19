html_layout='''
  <!DOCTYPE html>
  <html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <style>
    body {
        background-color: #ebbd34;
        font-family:"times new roman";
    }
    </style>
    <body>
   <div class="w3-top">
  <div class="w3-bar w3-white w3-padding w3-card" style="letter-spacing:4px;">
    <a href="#home" class="w3-bar-item w3-button">Creating Bee Awarness</a>
    <!-- Right-sided navbar links. Hide them on small screens -->
    <div class="w3-right w3-hide-small">
      <a href="#about" class="w3-bar-item w3-button">Why this project?</a>
      <a href="#history" class="w3-bar-item w3-button">Build Up</a>
      <a href="#analysis" class="w3-bar-item w3-button">Analysis</a>
      <a href="#conclusion" class="w3-bar-item w3-button">Conclusion</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="w3-display-container w3-content w3-wide" style="max-width:1600px;min-width:500px" id="home">
    <div class="w3-display-bottomleft w3-padding-large w3-opacity">
    </div>
  </header>

  <!-- Page content -->
  <div class="w3-content" style="max-width:1100px">

  <!-- Why this project  -->
  <div class="w3-row w3-padding-64" id="about">
    <div class="w3-col m6 w3-padding-large w3-hide-small">
     <img src="static/save_bees.jpg" class="w3-round w3-image w3-opacity-min" alt="Save Bees" width="600" height="750">
    </div>

    <div class="w3-col m6 w3-padding-large">
      <h1 class="w3-center"><b>Why this project?</b></h1><br>
      <h4 class="w3-center"><b>Inspiration</b></h4>
      <p class="w3-large">Over the past 15 years, bee colonies have been disappearing in what is known as the "colony collapse disorder". According to National Geographic some regions have seen losses of up to 90%. North American beekeepers reported a 37% loss in honeybee colonies last year(2019).</p>
         <img src="static/bee-thought1.jpg" class="w3-round w3-image w3-opacity-min" alt="Save Bees" width="600" height="750">
          <br>
          <br>
      <hr>
      <h4 class="w3-center"><b>Importance of Bees</b></h4>
      <p class="w3-large">According to the Food and Agriculture Organisation, bees are responsible for about 80% of pollination worldwide, making them vital to agriculture. Of the 100 crops that supply about 90% of the food for most of the world, 71 are pollinated by bees. Decline in bee population means fruit and vegetables are less available and hence more expensive.</p>
    </div>
  </div>
  <hr>
  <!--Story-->
  <div id="history">
  <p class="w3-large">In US there are more than 4000 native bee species. Bumble bees, metallic-green, sweat bees, squash bees and imported honey bee. There were no honeybees in America until the white settlers brought hives from Europe and that's why they are called imported. These bees remain unnoticed by most of us and yet they provide valuable services to all kinds of flowers, plants and various crops. Have you ever imagined how much does a bee worth? This is the era of capitalism and instead of focusing how bees are important for our environment, let us try to calculate how much a beehive contributes to our economy!</p>
      <br> 
      <p class="w3-large">Let's take an example of blueberry farm. Bee is a hard working creature. It is capable of visiting about 50,000 blueberry flowers in their short life span. This is enough to produce 6000 riped blueberries worth $20 at the market. On an average bee-hive consist of 20k-80k worker bees. If we average out the value of bee-hives just for producing riped blueberries it sums upto $1 Million!.</p>
      <br>
      <p class="w3-large">Beekeeping is an interesting topic. Some people say it affects natural habitat of bees while others consider it as a act of providing shelter. Where do you stand? The beekeeping industry is divided into 3 types of production:- Hobbyists , part-time and commercial. The former two consists of roughly 40% of honey production. Indicating that beekeeping is also a hobby rather than just commercial activity. In Slovenia, beekeeping is a way of life. In this small European nation of 2 million, 1 out of every 200 people is a beekeeper. According to the Food and Agriculture Organization (FAO) from 2007 to 2017, Slovenia saw a 57% increase in beehive numbers.</p>
      <br>
      <div class="fact-box">
      <h4 class="fun_fact_heading">Fun Fact</h4>
      <p>Most wasps are carnivores. Millions of years ago when flowering plants began to boom, these wasps started consuming pollen. It didn’t take much to find the advantages of consuming pollen over hunting. Pollen is also rich in proteins and doesn’t fight back so it is easy to imagine why they were happy to become vegetarians. This is how wasps descended into bees!</p>
      </div> 
      <p class="w3-large">Let's try to look into near past and analyse the situation of United States.</p> 
      <li class="w3-large">Reason for the decline of bee population in past years.</li>
      <li class="w3-large">Impact on bees in various states.</li>
      <li class="w3-large">Year wise analysis</li>
      <li class="w3-large">States with highest decline in bee colonies and Why?</li>
  </div>
  <br>
  <br>
    <br>
      <br>
        {%app_entry%}
          <!-- Site footer -->
    </div>
    <footer class="site-footer">
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <h6>More Details</h6>
            <p class="justify">Extensive data analysis and research was done before publishing this website. We did not want to overwhelm our readers by just shoving down data into their brains. Our motive was to create awareness. For all the data visualization and analytics savy people, link to github repository is down below. An Extensive use of libraries like pandas, matplotlib and seaborn was done to extract life out of this data.</p>
            <li><a href="https://github.com/mitul01/beeAwareness" target="_blank">Github Repository Link</a></li>
            </div>
          </div>
        </div>
      <hr>
         <div class="container">
          <div class="row">
            <div class="col-sm-12 col-md-6">
            <h6>Created By</h6>
              <h5>Mitul Tandon and Aanchal Tandon</h5>
              <h5>...............................</h5>            
            </div>
          </div>
        </div>
         <div class="container">
          <div class="row">
            <div class="col-sm-12 col-md-6">
            <h6>Follow Us<h6>
        <a href="https://twitter.com/TandonMitul" target="_blank"><img src="static/twitter.png" class="twitter"></img></a>
        <a href="https://www.linkedin.com/in/mitul-tandon-240842177/" target="_blank"><img src="static/linkedin.png" class="linkedin"></img></a>
        <a href="https://github.com/mitul01" target="_blank"><img src="static/github.png" class="github"></img></a>
        </div>
      </div>
    </div>
        {%config%}
        {%scripts%}
        {%renderer%}
</footer>
     </body>
  </html>
  '''


 