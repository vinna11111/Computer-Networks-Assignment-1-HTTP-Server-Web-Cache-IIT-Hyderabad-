# Computer-Networks-Assignment-1-HTTP-Server-Web-Cache-IIT-Hyderabad-
What I Built & Learned

🔹 1. HTTP Server
	•	Implemented a lightweight HTTP server from scratch.
	•	Supported operations:
	•	GET → Retrieve values
	•	PUT → Insert key-value pairs
	•	DELETE → Remove key-value pairs
	•	Designed a simple key-value store for request handling.
	•	Used pcap traces + Wireshark to verify correct HTTP communication.
	•	Learned how application-layer protocols (HTTP) ride over TCP sockets.

⸻

🔹 2. Web Cache
	•	Implemented a proxy cache that sits between client and server.
	•	Key learnings:
	•	Cache Hit → Response served instantly from cache.
	•	Cache Miss → Request forwarded to server, response cached for future.
	•	Observed how caching drastically reduces latency.
	•	Measured and compared end-to-end request timings across scenarios.

⸻

🔹 3. Network Measurement & Analysis
	•	Captured pcap traces at client, server, and cache nodes.
	•	Analyzed packet flows in Wireshark to validate protocol correctness.
	•	Compared timings across first, second, and third requests to quantify caching benefits.
	•	Learned how tools like Mininet emulate real-world topologies for reproducible experiments.

⸻

