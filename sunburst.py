import plotly.graph_objects as go

fig =go.Figure(go.Sunburst(
    labels=["Books", "Travel", "Sports & Outdoors", "Health, Fitness & Dieting", "Computers & Technology",
            "Medical Books", "New, Used & Rental Textbooks", "Science & Math", "Politics & Social Sciences",
            "History","Education & Teaching", "Reference", "Children's Books", "Biographies & Memoirs",
            "Literature & Fiction", "Crafts, Hobbies & Home", "Cookbooks, Food & Wine", "Science Fiction & Fantasy",
            "Arts & Photography", "Humor & Entertainment", "Christian Books & Bibles", "Religion & Spirituality",
            "Business & Money", "Teen & Young Adult", "Comics & Graphic Novels", "Engineering & Transportation",
            "Calendars", "Self-Help", "Law", "Mystery, Thriller & Suspense", "Parenting & Relationships",
            "Gay & Lesbian", "Romance"],
    parents=["", "Books", "Books", "Books", "Books", "Books", "Books", "Books", "Books",
             "Books", "Books", "Books", "Books", "Books", "Books", "Books", "Books",
             "Books", "Books", "Books", "Books", "Books", "Books", "Books", "Books"  ],
))
# Update layout for tight margin
# See https://plot.ly/python/creating-and-updating-figures/
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()

fig1 =go.Figure(go.Sunburst(
    labels=["Education & Teaching", "Schools & Teaching", "Studying & Workbooks", "Higher & Continuing Education"],
    parents=["", "Education & Teaching", "Education & Teaching", "Education & Teaching"],
))
# Update layout for tight margin
# See https://plot.ly/python/creating-and-updating-figures/
fig1.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig1.show()

fig2 =go.Figure(go.Sunburst(
    labels=["Studying & Workbooks", "Study Skills", "Study guide", "Workbooks"],
    parents=["", "Studying & Workbooks", "Studying & Workbooks", "Studying & Workbooks"],
))
# Update layout for tight margin
# See https://plot.ly/python/creating-and-updating-figures/
fig2.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig2.show()