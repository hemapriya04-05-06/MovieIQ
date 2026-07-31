import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="MovieIQ",
    page_icon="🎬",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    df = pd.read_csv("movies.csv")
    

    median_revenue = df["revenue"].median()

    df["success"] = (
        df["revenue"] > median_revenue
    ).astype(int)

    df["status"] = df["success"].map({
        1: "Success",
        0: "Failure"
    })

    return df

df = load_data()

# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():

    return joblib.load("model.pkl")

model = load_model()

def style_chart(fig):
    fig.update_layout(
        height=320,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#1F2937"),
        colorway=["#2563EB", "#60A5FA", "#93C5FD", "#DBEAFE"]
    )
    return fig

# =====================================================
# HEADER
# =====================================================

st.markdown("""

<div class="header">

<h1>🎬 MovieIQ</h1>

<p>
Movie Success Prediction Dashboard
</p>

</div>

""", unsafe_allow_html=True)

# =====================================================
# PREDICTION TITLE
# =====================================================

st.markdown(
"""
<h2 class='section-title'>
🎯 Movie Success Prediction
</h2>
""",
unsafe_allow_html=True
)

# =====================================================
# PREDICTION LAYOUT
# =====================================================

left,right = st.columns([2,1])

with left:

    budget = st.number_input(
        "Budget",
        min_value=0,
        value=50000000,
        step=1000000
    )

    popularity = st.number_input(
        "Popularity",
        value=50.0
    )

    runtime = st.number_input(
        "Runtime",
        value=120
    )

    vote_average = st.slider(
        "Vote Average",
        0.0,
        10.0,
        6.5
    )

    genre = st.selectbox(
        "Genre",
        sorted(df["genres"].unique())
    )

    predict = st.button(
        "🎬 Predict Movie Success",
        use_container_width=True
    )

with right:

    st.markdown("""

<div class="info-card">

<h3>Prediction Guide</h3>

Budget → Production Budget

Popularity → TMDB Popularity

Runtime → Minutes

Vote Average → IMDb/TMDB Rating

Genre → Movie Category

</div>

""",unsafe_allow_html=True)

# =====================================================
# PREDICTION
# =====================================================

if predict:

    input_df = pd.DataFrame({

        "budget":[budget],

        "popularity":[popularity],

        "runtime":[runtime],

        "vote_average":[vote_average],

        "genres":[genre]

    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    confidence = probability.max()*100

    st.markdown("---")

    if prediction==1:

        st.success(
            f"🎉 SUCCESS\n\nConfidence : {confidence:.2f}%"
        )

    else:

        st.error(
            f"❌ FAILURE\n\nConfidence : {confidence:.2f}%"
        )

st.markdown("---")

st.markdown(
"""
<h2 class='section-title'>
📊 Analytics Dashboard
</h2>
""",
unsafe_allow_html=True)

# =====================================================
# CHART LAYOUT
# =====================================================

row1_col1,row1_col2 = st.columns(2)

row2_col1,row2_col2 = st.columns(2)

row3_col1,row3_col2 = st.columns(2)

row4_col1,row4_col2 = st.columns(2)

# =====================================================
# CHART 1
# =====================================================

with row1_col1:

    st.subheader("🎯 Success Distribution")

    success = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    success.columns = ["Status","Count"]

    fig = px.pie(
        success,
        names="Status",
        values="Count",
        hole=0.65,
        color="Status",
        color_discrete_map={
            "Success":"#2563EB",
            "Failure":"#93C5FD"
        }
    )

    fig.update_layout(
        template="simple_white",
        height=380,
        legend_title="",
        margin=dict(l=10,r=10,t=30,b=10)
    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)


# =====================================================
# CHART 2
# =====================================================

with row1_col2:

    st.subheader("💰 Budget vs Revenue")

    fig = px.scatter(
        df,
        x="budget",
        y="revenue",
        color="popularity",
        hover_name="title",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        template="simple_white",
        height=380
    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)

    # =====================================================
# CHART 3
# =====================================================

with row2_col1:

    st.subheader("🎬 Genre Distribution")

    genre = (
        df["genres"]
        .value_counts()
        .reset_index()
    )

    genre.columns=["Genre","Count"]

    fig = px.bar(

        genre,

        x="Genre",

        y="Count",

        color="Count",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        template="simple_white",

        coloraxis_showscale=False,

        height=380

    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)


# =====================================================
# CHART 4
# =====================================================

with row2_col2:

    st.subheader("💵 Average Revenue by Genre")

    revenue = (

        df.groupby("genres")["revenue"]

        .mean()

        .reset_index()

        .sort_values(

            by="revenue",

            ascending=False

        )

    )

    fig = px.bar(

        revenue,

        x="genres",

        y="revenue",

        color="revenue",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        template="simple_white",

        coloraxis_showscale=False,

        height=380

    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)

    # =====================================================
# CHART 5
# =====================================================

with row3_col1:

    st.subheader("⭐ Popularity vs Revenue")

    fig = px.scatter(

        df,

        x="popularity",

        y="revenue",

        color="vote_average",

        hover_name="title",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        template="simple_white",

        height=380

    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)


# =====================================================
# CHART 6
# =====================================================

with row3_col2:

    st.subheader("⏱ Runtime Distribution")

    fig = px.histogram(

        df,

        x="runtime",

        nbins=20,

        color_discrete_sequence=["#2563EB"]

    )

    fig.update_layout(

        template="simple_white",

        height=380

    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)

    # =====================================================
# CHART 7
# =====================================================

with row4_col1:

    st.subheader("⭐ Vote Average Distribution")

    fig = px.histogram(

        df,

        x="vote_average",

        nbins=20,

        color_discrete_sequence=["#1D4ED8"]

    )

    fig.update_layout(

        template="simple_white",

        height=380

    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)


# =====================================================
# CHART 8
# =====================================================

with row4_col2:

    st.subheader("🔥 Correlation Heatmap")

    corr = df[

        [

            "budget",

            "revenue",

            "popularity",

            "runtime",

            "vote_average"

        ]

    ].corr()

    fig = px.imshow(

        corr,

        text_auto=".2f",

        color_continuous_scale="Blues",

        aspect="auto"

    )

    fig.update_layout(

        template="simple_white",

        height=380

    )

    style_chart(fig)
    st.plotly_chart(fig,use_container_width=True)