import solara

@solara.component
def Page():
    # Add a logo URL
    logo_url = "https://github.com/prosperwashaya/PS_POINTS/blob/master/logo2%20-%20Copy%20(2).png?raw=true"  # Replace with the link to your company logo

    # Navigation bar
    with solara.Column():
        with solara.Row():
            solara.Image(logo_url)  # Use native size or pre-scaled images
            # Title on the left
            solara.Markdown("## **GeoTown**: Shaping the Future of Geospatial Technology")
            # Logo on the right
            solara.Image(logo_url)  # Use native size or pre-scaled images

    # Main content
    with solara.Column():
        markdown = """
        ### Who We Are

        At **GeoTown**, we combine cutting-edge technology with expert geospatial knowledge to empower businesses, researchers, and decision-makers. From urban planning and environmental monitoring to disaster response and agriculture, we provide the tools you need to see the world differently.

        🚀 **Why GeoTown?**
        - Transform raw data into actionable insights.
        - Harness the power of remote sensing and satellite data.
        - Make better decisions with advanced geospatial analytics.

        ### What We Offer

        - **Interactive Web Apps:** Simplify complex geospatial workflows with intuitive tools.  
        - **Custom Solutions:** Tailored geospatial solutions to fit your unique challenges.  
        - **Expert Consultation:** Work alongside our geospatial experts to maximize your impact.  

        📍 **Our Mission**: To make geospatial intelligence accessible, actionable, and impactful for everyone.

        ### Explore Our Tools and Resources
        
        - 🌐 [GeoTown Web App](https://your-company-webapp-link): Start your geospatial journey with our flagship platform.  
        - 💻 [GitHub Repository](https://your-company-github-link): Dive into the code that powers our innovations.  
        - 🔗 [LinkedIn Profile](https://linkedin.com/company/geo-town): Connect with us for updates, insights, and opportunities.  

        ### Join the GeoTown Community!

        Be part of a thriving community of geospatial professionals and enthusiasts.  
        Follow us for the latest innovations, tutorials, and success stories in geospatial analysis.

        🌟 **Let’s transform the way we see and shape the world—together!**
        """
        solara.Markdown(markdown)

        # Call-to-action Buttons
        with solara.Row():
            solara.Button("Explore Web App", on_click=lambda: solara.navigate("https://your-company-webapp-link"))
            solara.Button("View on GitHub", on_click=lambda: solara.navigate("https://your-company-github-link"))
            solara.Button("Follow on LinkedIn", on_click=lambda: solara.navigate("https://www.linkedin.com/your-company-link"))
