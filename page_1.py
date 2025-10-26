def get_page_html(form_data):
    print("About to return Page 1...")

    page_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Global Vaccine Trends</title>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                text-align: center;
                background-color: #f9f9f9;
                color: #111;
            }

            header {
                background-color: #4da6ff;
                padding: 10px 0;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .header-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 90%;
                max-width: 1200px;
            }

            .logo {
                height: 45px;
            }

            input[type="search"] {
                padding: 8px 12px;
                border: none;
                border-radius: 20px;
                width: 260px;
            }

            nav a {
                margin-left: 15px;
                text-decoration: none;
                color: #000;
                font-weight: bold;
            }

            nav a:hover {
                color: #004c99;
            }

            h1 {
                margin-top: 35px;
                font-size: 32px;
                font-weight: bold;
            }

            h1 a {
                text-decoration: none;
                color: #111;
                transition: color 0.3s;
            }

            h1 a:hover {
                color: #4da6ff;
            }

            .facts {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 30px;
                margin-top: 30px;
                margin-bottom: 30px;
            }

            .fact-box {
                background: white;
                border: 2px solid #000;
                border-radius: 15px;
                width: 230px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease;
            }

            .fact-box:hover {
                transform: translateY(-5px);
            }

            .fact-box p {
                font-weight: bold;
                margin-bottom: 10px;
            }

            .fact-box a {
                text-decoration: none;
                color: #004c99;
            }

            .fact-box a:hover {
                text-decoration: underline;
            }

            .explore-btn {
                background-color: #4da6ff;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 25px;
                font-weight: bold;
                cursor: pointer;
                transition: background 0.3s;
            }

            .explore-btn:hover {
                background-color: #3385cc;
            }
        </style>
    </head>
    <body>

        <header>
            <div class="header-content">
                <div class="left-section">
                    <img src="download.png" alt="WHO Logo" class="logo" />
                </div>

                <div class="middle-section">
                    <input type="search" placeholder="Search..." />
                </div>

                <nav class="right-section">
                    <a href="/">Home</a>
                    <a href="page_2.html">Vaccination Rates</a>
                    <a href="page_3.html">Vaccine Trends</a>
                    <a href="#">Contact</a>
                </nav>
            </div>
        </header>

        <h1><a href="page_3.html">Global Vaccine Trends</a></h1>

        <div class="facts">
            <div class="fact-box">
                <a href="page_2.html">
                    <p>Vaccination rates by country/region</p>
                </a>
            </div>

            <div class="fact-box">
                <a href="page_3.html">
                    <p>Countries with biggest vaccination improvement</p>
                </a>
            </div>

            <div class="fact-box">
                <p>Mission Statement<br>(purpose, personas, team info)</p>
            </div>

            <div class="fact-box">
                <p>Infection data by economic status</p>
            </div>

            <div class="fact-box">
                <p>Countries above average infection rate</p>
            </div>
        </div>

        <button class="explore-btn" onclick="window.location.href='page_3.html'">EXPLORE MORE</button>

    </body>
    </html>
    """
    return page_html

