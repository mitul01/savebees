import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from layout import html_layout

external_stylesheets =["https://www.w3schools.com/w3css/4/w3.css"]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
server=app.server
app.title="SaveBees"
# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("static/intro_bees.csv")
# ------------------------------------------------------------------------------
app.index_string=html_layout
# App layout
app.layout = html.Div([
    # Table
    #header
    html.Div(children=[
    #html.H1("Let's Analyse", style={'text-align': 'center','color':'black'}),
    html.Div(children=[   
    dcc.Dropdown(id="slct_year_map",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container_map', children=[],style={'text-align': 'left','color':'black','bold':True}),
    html.Br(),
    dcc.Graph(id='my_bee_map', figure={},config={'displayModeBar':False,'scrollZoom':False,'responsive':False},
        style={'width':"110%"}),
    html.Hr(),
    html.Br(),
    html.H1(id="analysis",children=html.B("Factors affecting bees"),style={'text-align':'center','color':'black','font-family': 'cursive',}),
    ]),
    html.Br(),
    html.Div([html.Img(src="static/graph1.png",className='center')]),
    html.Br(),
    html.H4(html.B("The big question. Why is it happening? Why are bees disappearing? Are we humans responsible for this?")),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.P("Researchers who are leading this effort have come out with several reasons. We listed few of these reasons and collected data from United States Department of Agriculture and investigated it. As you can see above one of the many graphs that we plotted during our study revealed some of the major factors affecting the bees. Top assassinator being Varroa Mites."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.H5(html.B("Varroa Mites")),
    html.P("Varroa mites were originally found only in Asia, as parasites, on the imported European honeybee in 1963. They appeared next in various countries in Europe and South America in the early- to mid-70's. It was not until 1979 when a single mite was discovered in Maryland and then they began to spread across the entire USA around 1987. In its original host (Asian Honeybees) the mite causes much less mortality but, in the Americas, they are decimating feral populations. These mites feed off of larvae and adults. By crippling adults and killing potential workers at the larval stage, varroa infestation weakens the colony, leaving it open to conquest by other colonies or the eventual death of the infested colony due to lack of maintenance. According to the given data, we were able to estabilish a pattern. In the months of July-September when temperatures are soaring high in states like Florida, California, Hawaii etc. varroa mite infestation kills an entire colony within seven months. This result is astonishing because typically mites require about 3-4 years to wipe out an entire colony."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.H5(html.B("Diseases")),
    html.P("Every living species on this planet suffer from diseases ranging from bacterial to viral. New or emerging diseases such as Israeli Acute Paralysis virus and the gut parasite Nosema are major concerns right now. I hope everyone can relate how a disease can kill a species after experiencing pandemic. Moreover, bees don’t have doctors among them as we do."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.H5(html.B("Pesticides")),
    html.P("Farmers love to use pesticides. They either sprinkle these chemicals directly on top of crops or coat seeds while sowing them to boost their growth. In both cases pesticides are absorbed by plants thus developing poisonous pollen grains and nectar for insects. Our analysis reveals an increase in death of bees by pesticides. In 2018 almost 8% of bees died due to pesticides in the entire USA. So, we dig deeper. The use of neonicotinoids  (a type of pesticide) is devastating for bees. Since the introduction of neonics, U.S. agriculture has become 48 times more toxic to bees and other insects! The neonic coating on one corn seed has enough active ingredient to kill about a quarter million bees. As we move forward, these pesticides are being discouraged. As a matter of fact, anything prepared artificially being introduced in environment is bound to effect it in some way or the other. Use of natural made products can only save us from this sin."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.H5(html.B("Others/Unknown")),
    html.P("These factors are open to interpretation for readers. But mainly they consist of destruction of beehives due to human interference. The increased use of electromagnetic wave is believed to kill many insects like bees, butterflies. Bees experience lot of stress in their community while being transported to multiple locations across the country for providing pollination services. Other reasons include changes to the habitat where bees forage, poor nutrition etc."),
    ]),
    html.Br(),
    html.Hr(),
    html.H1(html.B("State-wise representation of impact on bee colonies"),style={'text-align':'center','color':'black','font-family': 'cursive',}),
    html.Br(),
    html.Br(),
# ------------------------------------------------------------------------------
    html.Div([
    dcc.Dropdown(id="slct_year_bar",
                 options=[
                     {"label": "2015 vs 2016", "value":"2015 vs 2016" },
                     {"label": "2016 vs 2017", "value":"2016 vs 2017"},
                     {"label": "2017 vs 2018", "value":"2017 vs 2018"},
                     {"label": "2018 vs 2019(Jan-Mar)", "value":"2018 vs 2019(Jan-Mar)"},
                     ],
                 multi=False,
                 value="2017 vs 2018",
                 style={'width': "50%",}
                 ),
    html.Br(),
    dcc.Graph(id='states_Vs_Colonies',figure={},),
    html.Br(),
    html.Div(style={'font-family':'times new roman','font-size':'18px','display':'inline-flex'},children=[
    html.Img(src="static/hawaii.png",style={'width':'50%','height':'50%'}),    
    html.P("In early 1900’s, Bees were considered Hawaii’s most abundant insect. Because of reasons such as habitual degradation, invasive species, agricultural pesticides, and sea level rise led to decline in bee colonies. Hawaii’s bees are harmed by ants, studies have found ants invade yellow-faced bee nests and feast on the unborn larvae. According to our analysis almost 50% of bees are each affected by pests like ants and Varroa mites. Since Hawaii is a coastal area most of the bees like to nest in the hollows of certain native coastal plant species or even in holes of coral rocks. Thus, making them prone to tsunamis or even sea level rise. Tsunamis have even whipped out the entire bee colonies in some regions of Hawaii."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.P("The biggest problem in Florida is the varroa mite, which is one of the pieces of this puzzle. Almost 25% bees have died due to mites in past years. High soaring temperatures in Florida in the months of July-Sept just makes this situation worse .The next major problem in Florida is citrus greening. Tiny insects produce a bacterium that shuts down the tree's flow of sap, producing poisonous nectar for bees. Bees are hardworking but not smart and they feed on this nectar and eventually die."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.P("Neonicotinoids are incredibly toxic to bees and other insects. Among all toxic pesticides used almost 92% of bees are affected by neonics.According to the data we investigated, during 2015-2018, nearly 15% and 10% of bee colonies were diminished in Florida and New Mexico respectively only by the use of pesticides. Other reasons like global warming, habitat loss, parasite prevail in New Mexico."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px','display':'inline-flex'},children=[
    html.P("With millions of acres of farmland, California leads the U.S. in agricultural production. World’s famous California Almonds are everywhere in the world. Around 50-80% of almonds supplied in world are produced in California. And yes you guessed it right! Bees are responsible for pollination of almonds. Bees and almonds are like Coffee and Cream. Bee population is declining in Florida. There is not enough local bees due to which bees are transported from other places into California. This exploitation does affect bees. Moreover, pesticides being used in almonds are also affecting bees. In many cases farmers mix insecticides and fungicides (used for crop protection). Studies show that some combinations are deadly to bees."),
    html.Img(src="static/california.png",style={'width':'50%','height':'50%'}),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.P("Importance of bees is not a new topic and still we are failing to save the bees. Although we have to be optimistic. It is important to see the data from both the sides. I would like to point out some states like Connecticut, Nebraska, Maryland, New Jersey are comparatively doing better than others. There is no magic wand, we must come through and protect the ecosystem."),
    ]),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.P("Various states have enforced laws to protect the bee colonies. Let us discuss few of these steps which have helped:"),
    html.Li("Research is key to any problem. In 2016 Connecticut, Virginia, Oklahoma authorized their department of Agriculture to develop a pollinator protection strategy. University of Minnesota are actively doing research on such topics."),
    html.Li("Pesticides is one thing that humans can directly control and take rapid steps to trickle down this problem. Number of bee colonies affected in Vermont decreased from 11.7% in 2017 to 5.6% in 2018. Moreover, in the 1st quarter of 2019 only 1.9% bees were affected. This came after strict regulation of the sale and application of neonicotinoid pesticides. After seeing such results in many more states like Nebraska and Maryland, Hawaii also adopted the same route in 2019."),
    html.Li("Beekeeping is other solution that is being promoted in USA. It is a commercial activity that helps to maintain the balance of ecosystem. Ironic! isn’t it? Beekeeping is being heavily promoted in places like California, Iowa, Washington etc. where there is urgent need to increase bee colonies. To be honest beekeeping is just a desperate measure and not a practical solution to this problem."),
    ]),
    html.Br(),
    ]),
    html.Hr(),
# ------------------------------------------------------------------------------
    html.Div(id="conclusion",children=[
    html.H1(html.B("Conclusion"),style={'text-align':'center','color':'black','font-family': 'cursive',}),
    html.Div(style={'font-family':'times new roman','font-size':'18px'},children=[
    html.P("We hope you took some great insights from our study. We created this website to increase awareness among the society. Bees are essential part of our ecosystem and no we do not want artificial pollinators flying in the skies in future. Some of the pieces of this puzzle are still missing and we heavily rely on ongoing research to find something more meaningful that helps us to protect these little hard-working creatures."),
    html.P("Meanwhile, things every person can do to help save the bees:"),
    html.Li("Keep bee friendly plants (like Lavender, mahonia , rosemary)."),
    html.Li("Support your local beekeepers."),
    html.Li("Avoid using pesticides or chemical outside in gardening."),
    html.Li("Keep a bowl of water outside with some stones, cork for them to land on."),
    html.Li("Sponsor a hive "),
    html.Li("Spread awareness (share this website 😉)"),
    html.Li("Start your own hive (this would be wild though)"),
    ]),
    ]),
# ----------------------------------------------------------------------------
    html.Br(),
    html.Br(),
]),
])
# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
 # ------------------------------------------------------------------------------   
@app.callback(
    [Output(component_id='output_container_map', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year_map', component_property='value')]
)
def map_graph(option_slctd):

    container = "The year chosen by user is: {}".format(option_slctd)

    dff = df.copy()

    dff = dff.groupby(['State','Year','state_code'])[['Pct of Colonies Impacted']].mean()
    dff.reset_index(inplace=True)
    dff = dff[dff["Year"] == option_slctd]
    # Plotly Express
    fig1 = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        template='ggplot2',
        labels={'Pct of Colonies Impacted': '% of Bee Colonies Impacted'},
    )
    fig1.update_layout(paper_bgcolor='#ebbd34',margin=dict(l=0,r=0,t=0,b=0))

    return container, fig1
# ------------------------------------------------------------------------------
@app.callback(
     Output(component_id='states_Vs_Colonies', component_property='figure'),
     [Input(component_id='slct_year_bar', component_property='value')])
def bar_graph(option_slctd):
   
    if option_slctd!=None:

        if option_slctd =="2017 vs 2018":
            dff = df.copy()
            dff = dff.groupby(['State','Year','state_code'])[['Pct of Colonies Impacted']].mean()
            dff.reset_index(inplace=True)
            dff=dff[dff['Year']!=2019]
            dff=dff[dff['Year']!=2015]
            dff=dff[dff['Year']!=2016]
            fig=px.line(dff,x='State',y='Pct of Colonies Impacted',color='Year')

        elif option_slctd =="2016 vs 2017":
            dff = df.copy()
            dff = dff.groupby(['State','Year','state_code'])[['Pct of Colonies Impacted']].mean()
            dff.reset_index(inplace=True)
            dff=dff[dff['Year']!=2019]
            dff=dff[dff['Year']!=2015]
            dff=dff[dff['Year']!=2018]
            dff=dff.groupby(['State','Year'])[['Pct of Colonies Impacted']].mean().reset_index()
            fig=px.line(dff,x='State',y='Pct of Colonies Impacted',color='Year')

        elif option_slctd =="2015 vs 2016":
            dff = df.copy()
            dff = dff.groupby(['State','Year','state_code'])[['Pct of Colonies Impacted']].mean()
            dff.reset_index(inplace=True)
            dff=dff[dff['Year']!=2019]
            dff=dff[dff['Year']!=2017]
            dff=dff[dff['Year']!=2018]
            dff=dff.groupby(['State','Year'])[['Pct of Colonies Impacted']].mean().reset_index()
            fig=px.line(dff,x='State',y='Pct of Colonies Impacted',color='Year')

        elif option_slctd =="2018 vs 2019(Jan-Mar)":
            dff = df.copy()
            dff = dff.groupby(['State','Year','state_code','Period'])[['Pct of Colonies Impacted']].mean()
            dff.reset_index(inplace=True)
            dff=dff[dff['Period']=="JAN THRU MAR"]
            dff=dff[dff['Year']!=2015]
            dff=dff[dff['Year']!=2017]
            dff=dff[dff['Year']!=2016]
            dff=dff.groupby(['State','Year'])[['Pct of Colonies Impacted']].mean().reset_index()
            fig=px.line(dff,x='State',y='Pct of Colonies Impacted',color='Year')
    else:
        fig=px.line()

    fig.update_layout(title="Impact on bees across USA",paper_bgcolor='#ebbd34',margin=dict(r=5,l=5),title_font_family='cursive')
    return fig
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)