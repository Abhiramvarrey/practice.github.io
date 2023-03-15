<!DOCTYPE html>
<html>
<head>
	<title>Event Website</title>
	<link rel="stylesheet" type="text/css" href="testme.css">
</head>
<body>
	<header>
		<nav>
			<ul>
				<li><a href="#">Home</a></li>
				<li><a href="#">About</a></li>
				<li><a href="#">Events</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
		</nav>
	</header>

	<section class="hero-section">
		<h1>Welcome to our Event</h1>
		<p>Join us for an exciting and fun-filled event</p>
		<button>Register Now</button>
	</section>

	<section class="about-section">
		<h2>About the Event</h2>
		<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
	</section>

	<section class="events-section">
		<h2>Events Schedule</h2>
		<ul>
			<li>
				<h3>Event 1</h3>
				<p>Date: 15th April 2023</p>
				<p>Time: 10:00 AM - 12:00 PM</p>
				<p>Venue: ABC Hall</p>
			</li>
			<li>
				<h3>Event 2</h3>
				<p>Date: 16th April 2023</p>
				<p>Time: 2:00 PM - 4:00 PM</p>
				<p>Venue: XYZ Hall</p>
			</li>
		</ul>
	</section>

	<section class="contact-section">
		<h2>Contact Us</h2>
		<form>
			<label for="name">Name:</label>
			<input type="text" id="name" name="name" required>

			<label for="email">Email:</label>
			<input type="email" id="email" name="email" required>

			<label for="message">Message:</label>
			<textarea id="message" name="message" required></textarea>

			<button type="submit">Submit</button>
		</form>
	</section>

	<footer>
		<p>&copy; 2023 Event Website. All rights reserved.</p>
	</footer>
</body>
</html>
