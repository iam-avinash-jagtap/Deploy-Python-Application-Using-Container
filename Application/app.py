from flask import Flask
app = Flask(__name__)

@app.route('/')
def tech_aj_home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Welcome to Tech-AJ</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f0f4f8;
                color: #333;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #001f3f;
                color: white;
                padding: 20px;
                text-align: center;
            }
            nav {
                background-color: #003366;
                padding: 10px;
                text-align: center;
            }
            nav a {
                color: white;
                margin: 0 15px;
                text-decoration: none;
                font-weight: bold;
            }
            section {
                padding: 40px;
                max-width: 1000px;
                margin: auto;
                background-color: white;
                margin-top: 20px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
            }
            h2 {
                color: #003366;
            }
            footer {
                text-align: center;
                background-color: #001f3f;
                color: white;
                padding: 20px;
                margin-top: 30px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Tech-AJ</h1>
            <p>Your one-stop hub for everything tech – from gadgets to engines!</p>
        </header>

        <nav>
            <a href="#mobiles">Mobiles</a>
            <a href="#laptops">Laptops</a>
            <a href="#bikes">Bikes</a>
            <a href="#cars">Cars</a>
            <a href="#about">About Us</a>
            <a href="#contact">Contact</a>
        </nav>

        <section id="mobiles">
            <h2>📱 Mobile Zone</h2>
            <p>
                Stay up-to-date with the latest in mobile technology. At Tech-AJ, we cover flagship devices, budget phones, OS comparisons, and performance reviews.
                We test the top mobile processors, RAM performance, camera benchmarking, and battery life endurance across brands like Apple, Samsung, OnePlus, and Xiaomi.
                Whether you’re a gamer, a creator, or a minimalist user, we help you find your perfect match.
            </p>
        </section>

        <section id="laptops">
            <h2>💻 Laptop Insights</h2>
            <p>
                From ultrabooks to heavy-duty workstations, Tech-AJ breaks down laptops by performance, use-case, and value for money.
                We dive deep into CPU generations, GPU capabilities (NVIDIA vs AMD), thermal performance, and build quality.
                Expect expert reviews on developer laptops, student laptops, and gaming beasts.
            </p>
        </section>

        <section id="bikes">
            <h2>🏍️ Bike Garage</h2>
            <p>
                We review and analyze bikes from commuter models to high-performance machines. Our reports focus on mileage, build quality, engine efficiency,
                maintenance costs, and rider comfort. Brands like Yamaha, Bajaj, KTM, Royal Enfield, and Honda are covered extensively.
                Riders looking for the best 150cc, 250cc, or long-ride touring bikes will find honest comparisons and real-world experience breakdowns.
            </p>
        </section>

        <section id="cars">
            <h2>🚗 Car Zone</h2>
            <p>
                Dive into detailed reviews and breakdowns of cars ranging from hatchbacks to electric SUVs. At Tech-AJ, we evaluate engine performance, safety features,
                mileage, build quality, and infotainment systems. We also cover the future of mobility: EV technology, charging infrastructure, and autonomous features.
                Brands like Tata, Mahindra, Hyundai, Maruti, MG, and Tesla are reviewed with unbiased insights.
            </p>
        </section>

        <section id="about">
            <h2>📘 About Us</h2>
            <p>
                Tech-AJ was founded by Avinash Jagtap, a passionate tech enthusiast and computer science graduate (BSc + MSc) with a focus on modern technologies.
                Starting as a student in Solapur and now based in Pune, Avi’s journey includes web development, cloud computing, and DevOps engineering.
                <br><br>
                He has hands-on experience with AWS (EC2, S3, VPC, CloudFormation, IAM, etc.), Azure Admin, and has strong knowledge in Linux, networking, and system automation.
                Tech-AJ reflects his love for learning, reviewing, and simplifying tech for everyone – from students to professionals.
                <br><br>
                His goal? To become a top-tier DevOps Engineer and build scalable digital platforms that solve real-world problems.
            </p>
        </section>

        <section id="contact">
            <h2>📞 Contact Us</h2>
            <p>Got a question, review request, or collaboration idea?</p>
            <p><strong>Call Us:</strong> 8888474060</p>
            <p><strong>Email:</strong> (Coming Soon)</p>
        </section>

        <footer>
            <p>&copy; 2025 Tech-AJ. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
