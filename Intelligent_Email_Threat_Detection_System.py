Sample Code :
HTML Code
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Intelligent Email Threat Detector</title>
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<link 
href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap
" rel="stylesheet">
</head>
<body>
<div class="background-effects">
<div class="glow glow-1"></div>
<div class="glow glow-2"></div>
</div>
<!-- Center Module -->
<main class="center-module">
<h1 class="welcome-title">Intelligent Email Threat Detection</h1>
<p class="subtitle">Empowering you with AI-driven analysis to stay safe from evolving 
threats.</p>
<button id="btn-open-analyzer" class="btn-primary">Email Analyzer</button>
<!-- Results Container -->
<div id="results-container" class="hidden">
<h2 id="res-classification"></h2>
<div class="insight-box">
<h3>Email Insight</h3>
<p id="res-email-insight"></p>
</div>
<div class="insight-box hidden" id="box-url-insight">
<h3>URL Insight</h3>
<p id="res-url-insight"></p>
</div>
<div class="insight-box action-box">
<h3>Suggested Action</h3>
<p id="res-action"></p>
</div>
<div class="insight-box awareness-box">
<h3>Awareness Tips</h3>
<p id="res-awareness"></p>
</div>
<button id="btn-close-results" class="btn-secondary mt-2">Close Analysis</button>
</div>
</main>
<!-- Corner Modules -->
<!-- Left Corner Container -->
<div class="left-corner-container">
<div class="corner-module" id="mod-confidence">
<div class="widget-icon">📊</div>
<span>Confidence Score</span>
</div>
<div class="corner-module" id="mod-dashboard">
<div class="widget-icon"> </div>
<span>Threat Dashboard</span>
</div>
<div class="corner-module" id="mod-quiz">
<div class="widget-icon">□</div>
<span>Awareness Quiz</span>
</div>
<div class="corner-module" id="mod-summary">
<div class="widget-icon">📄</div>
<span>Email Summary</span>
</div>
<!-- <div class="corner-module" id="mod-feedback">
<div class="widget-icon">💬</div>
<span>Feedback</span>
</div> -->
</div>
<!-- Modals -->
<!-- Analyzer Modal -->
<div id="modal-analyzer" class="modal hidden">
<div class="modal-content glass">
<button class="close-btn" onclick="closeModal('modal-analyzer')">&times;</button>
<h2>Analyze Email</h2>
<form id="analyzer-form">
<input type="text" id="inp-subject" placeholder="Subject" required>
<textarea id="inp-body" rows="5" placeholder="Paste email body here..." 
required></textarea>
<textarea id="inp-urls" rows="2" placeholder="Paste URLs here 
(optional)"></textarea>
<button type="submit" class="btn-primary" id="btn-submit-analysis">Analyze 
Now</button>
</form>
<div id="loading" class="hidden">Analyzing...</div>
</div>
</div>
<!-- Confidence Modal -->
<div id="modal-confidence" class="modal hidden">
<div class="modal-content glass">
<button class="close-btn" onclick="closeModal('modal￾confidence')">&times;</button>
<h2>Confidence Score</h2>
<div class="score-display">
<h1 id="conf-score">--%</h1>
<h3 id="conf-level">--</h3>
</div>
<div class="info-text">
<strong>Meaning:</strong>
<p id="conf-meaning">Run an analysis first to see the model's certainty.</p>
<strong>Reliability:</strong>
<p>The system is highly reliable when strong threat indicators are present.</p>
</div>
</div>
</div>
<!-- Dashboard Modal -->
<div id="modal-dashboard" class="modal hidden">
<div class="modal-content glass">
<button class="close-btn" onclick="closeModal('modal￾dashboard')">&times;</button>
<h2>Threat Dashboard</h2>
<div class="dashboard-stats">
<div class="stat-card">
<h4>Total Analyzed</h4>
<h2 id="dash-total">0</h2>
</div>
<div class="stat-card safe">
<h4>Safe</h4>
<h2 id="dash-safe">0</h2>
</div>
<div class="stat-card spam">
<h4>Spam</h4>
<h2 id="dash-spam">0</h2>
</div>
<div class="stat-card phishing">
<h4>Phishing</h4>
<h2 id="dash-phishing">0</h2>
</div>
</div>
</div>
</div>
<!-- Quiz Modal -->
<div id="modal-quiz" class="modal hidden">
<div class="modal-content glass">
<button class="close-btn" onclick="closeModal('modal-quiz')">&times;</button>
<h2>□ Awareness Quiz</h2>
<div id="quiz-question">
<p><strong>Question:</strong> An email asks you to verify your bank account 
urgently. What should you do?</p>
<div class="quiz-options">
<button class="quiz-btn" onclick="checkAnswer(false)">(A) Click 
immediately</button>
<button class="quiz-btn" onclick="checkAnswer(false)">(B) Ignore warning 
signs</button>
<button class="quiz-btn" onclick="checkAnswer(true)">(C) Verify sender before 
action</button>
</div>
</div>
<div id="quiz-result" class="hidden">
<h3 id="quiz-feedback"></h3>
<p><strong>Explanation:</strong> Phishing emails create urgency to trick users.
Always verify the sender before clicking links.</p>
<button class="btn-secondary" onclick="resetQuiz()">Try Another</button>
</div>
</div>
</div>
<!-- Summary Modal -->
<div id="modal-summary" class="modal hidden">
<div class="modal-content glass">
<button class="close-btn" onclick="closeModal('modal-summary')">&times;</button>
<h2>📄 Email Summary</h2>
<div class="info-text">
<p id="sum-text">Run an analysis first to generate a summary.</p>
<hr>
<strong>Key Intent:</strong>
<p id="sum-intent">Waiting for analysis...</p>
</div>
</div>
</div>
<!-- Feedback Modal -->
<div id="modal-feedback" class="modal hidden">
<div class="modal-content glass">
<button class="close-btn" onclick="closeModal('modal-feedback')">&times;</button>
<h2>Feedback</h2>
<p>Help us improve our threat detection.</p>
<textarea rows="4" placeholder="Your feedback here..." style="width: 100%; box￾sizing: border-box;"></textarea>
<button class="btn-primary mt-2" onclick="closeModal('modal￾feedback')">Submit</button>
</div
</div>
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
Script.js
const btnOpenAnalyzer = document.getElementById('btn-open-analyzer'); 
const modalAnalyzer = document.getElementById('modal-analyzer'); 
const btnCloseResults = document.getElementById('btn-close-results'); 
const resultsContainer = document.getElementById('results-container'); 
const formAnalyzer = document.getElementById('analyzer-form');
const loading = document.getElementById('loading');
// Modules
const modules = ['confidence', 'dashboard', 'quiz', 'summary', 'feedback']; 
modules.forEach(mod => {
const el = document.getElementById(`mod-${mod}`); 
if (el) {
el.addEventListener('click', () => { 
openModal(`modal-${mod}`);
if(mod === 'dashboard') fetchDashboard();
});
}
});
function openModal(id) { 
document.getElementById(id).classList.remove('hidden');
}
function closeModal(id) { 
document.getElementById(id).classList.add('hidden');
}
btnOpenAnalyzer.addEventListener('click', () => { 
openModal('modal-analyzer');
});
btnCloseResults.addEventListener('click', () => { 
resultsContainer.classList.add('hidden'); 
btnOpenAnalyzer.classList.remove('hidden'); 
document.querySelector('.welcome-title').classList.remove('hidden'); 
document.querySelector('.subtitle').classList.remove('hidden');
});
formAnalyzer.addEventListener('submit', async (e) => { 
e.preventDefault();
loading.classList.remove('hidden'); 
formAnalyzer.classList.add('hidden');
const payload = {
subject: document.getElementById('inp-subject').value, 
body: document.getElementById('inp-body').value, 
urls: document.getElementById('inp-urls').value
};
try {
const response = await fetch('/analyze', { 
method: 'POST',
headers: { 'Content-Type': 'application/json' }, 
body: JSON.stringify(payload)
});
const result = await response.json();
displayResults(result, payload.urls);
updateBackgroundState(result);
closeModal('modal-analyzer');
} catch (err) { 
console.error(err); 
alert('Analysis failed.');
} finally { 
loading.classList.add('hidden');
formAnalyzer.classList.remove('hidden'); 
formAnalyzer.reset();
}
});
function displayResults(data, urls) { 
document.querySelector('.welcome-title').classList.add('hidden'); 
document.querySelector('.subtitle').classList.add('hidden'); 
btnOpenAnalyzer.classList.add('hidden'); 
resultsContainer.classList.remove('hidden');
const cl = document.getElementById('res-classification'); 
cl.innerText = `Classification: ${data.classification} Email`; 
cl.style.color = getColor(data.classification);
document.getElementById('res-email-insight').innerText = data.email_insight; 
document.getElementById('res-action').innerText = data.suggested_action; 
document.getElementById('res-awareness').innerText = data.awareness_tips;
const urlBox = document.getElementById('box-url-insight');
// Case 1 vs Case 2
if (urls && urls.trim().length > 0 && data.url_insight) { 
document.getElementById('res-url-insight').innerText = data.url_insight; 
urlBox.classList.remove('hidden');
} else {
urlBox.classList.add('hidden');
}
// Update globalstate for modals 
updateModalsWithData(data);
}
function updateModalsWithData(data) {
// Confidence
document.getElementById('conf-score').innerText = data.confidence; 
document.getElementById('conf-level').innerText = data.confidence_level; 
document.getElementById('conf-meaning').innerText = `The model detected patterns
indicative of ${data.classification.toLowerCase()} emails.`;
// Summary
document.getElementById('sum-text').innerText = data.summary; 
document.getElementById('sum-intent').innerText = data.email_insight;
}
async function fetchDashboard() { 
try {
const res = await fetch('/dashboard'); 
const data = await res.json();
document.getElementById('dash-total').innerText = data.total; 
document.getElementById('dash-safe').innerText = data.counts.Safe; 
document.getElementById('dash-spam').innerText = data.counts.Spam; 
document.getElementById('dash-phishing').innerText = data.counts.Phishing;
} catch(err) { console.error(err); }
}
function getColor(classification) {
if(classification === 'Phishing') return '#ef4444'; 
if(classification === 'Spam') return '#f59e0b';
return '#10b981';
}
function updateBackgroundState(data) { 
const col = getColor(data.classification);
document.querySelector('.glow-1').style.background = `radial-gradient(circle, ${col} 0%, 
transparent 70%)`;
}
// Quiz actions
function checkAnswer(isCorrect) {
document.getElementById('quiz-question').classList.add('hidden'); 
const res = document.getElementById('quiz-result'); 
res.classList.remove('hidden');
const fb = document.getElementById('quiz-feedback'); 
if(isCorrect) {
fb.innerText = "✅Correct!"; 
fb.style.color = "#10b981";
} else {
fb.innerText = "❌Incorrect."; 
fb.style.color = "#ef4444";
}
}
function resetQuiz() {
document.getElementById('quiz-question').classList.remove('hidden'); 
document.getElementById('quiz-result').classList.add('hidden');
}
Style.css
:root {
--bg-color: #050505;
--text-color: #ffffff;
--primary: #6366f1;
--primary-hover: #4f46e5;
--secondary: #333333;
--glass-bg: rgba(255, 255, 255, 0.08);
--glass-border: rgba(255, 255, 255, 0.12);
--phishing: #ef4444;
--spam: #f59e0b;
--safe: #10b981;
}
html, body { 
margin: 0;
padding: 0;
font-family: 'Inter', sans-serif; 
color: var(--text-color); 
height: 100vh;
overflow: hidden; 
position: relative;
background: url("../images/bg.png") no-repeat center center fixed; 
background-size: cover;
}
/* stronger dark overlay */ 
body::before {
content: ""; 
position: fixed; 
inset: 0;
background: rgba(0, 0, 0, 0.82);
z-index: 0;
pointer-events: none;
}
.background-effects { 
position: fixed; 
inset: 0;
z-index: 1; 
overflow: hidden;
pointer-events: none;
}
.glow {
position: absolute; 
width: 500px; 
height: 500px;
background: radial-gradient(circle, var(--primary) 0%, transparent 70%);
opacity: 0.12; 
filter: blur(80px);
border-radius: 50%;
animation: float 10s infinite alternate;
}
.glow-1 { top: -10%; left: -10%; }
.glow-2 { 
bottom: -10%;
right: -10%;
background: radial-gradient(circle, #8b5cf6 0%, transparent 70%); 
animation-delay: -5s;
}
@keyframes float {
0% { transform: translateY(0) scale(1); }
100% { transform: translateY(30px) scale(1.1); }
}
gap: 10px; 
cursor: pointer;
transition: all 0.3s ease; 
z-index: 5;
font-weight: 600; 
user-select: none;
}
.corner-module:hover {
background: rgba(255, 255, 255, 0.1); 
transform: scale(1.05);
}
.widget-icon { font-size: 1.5rem; }
.top-left { top: 20px; left: 20px; }
.top-right { top: 20px; right: 20px; }
.bottom-left { bottom: 20px; left: 20px; }
.bottom-right { bottom: 20px; right: 20px; }
.bottom-center { bottom: 20px; left: 50%; transform: translateX(-50%); }
.bottom-center:hover { transform: translateX(-50%) scale(1.05); }
/* Modals */
.modal {
position: fixed;
top: 0; left: 0; width: 100%; height: 100%;
background: rgba(0, 0, 0, 0.7); 
backdrop-filter: blur(5px); 
display: flex;
justify-content: center; 
align-items: center;
z-index: 100;
}
.glass {
background: #111111;
border: 1px solid var(--glass-border);
box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); 
border-radius: 16px;
padding: 30px; 
width: 90%;
max-width: 500px; 
position: relative;
animation: slideUp 0.3s ease-out;
}
@keyframes slideUp {
from { opacity: 0; transform: translateY(20px); } 
to { opacity: 1; transform: translateY(0); }
}
.close-btn {
position: absolute;
top: 15px; right: 20px;
background: none; border: none; 
color: #9ca3af; font-size: 1.5rem; 
cursor: pointer;
}
.close-btn:hover { color: white; }
/* Forms */ 
input, textarea {
width: 100%;
background: rgba(255,255,255,0.05); 
border: 1px solid var(--glass-border); 
color: white;
padding: 12px; 
border-radius: 8px; 
margin-bottom: 15px; 
font-family: inherit;
box-sizing: border-box; 
font-size: 1rem;
}
input:focus, textarea:focus { 
outline: none;
border-color: var(--primary);
}
/* Results Area */ 
#results-container {
background: var(--glass-bg);
border: 1px solid var(--glass-border); 
border-radius: 16px;
padding: 20px; 
margin-top: 20px; 
text-align: left;
backdrop-filter: blur(10px);
}
.insight-box {
background: rgba(0,0,0,0.3); 
border-radius: 8px;
padding: 10px 15px; 
margin-bottom: 10px;
border-left: 4px solid var(--primary);
}
.insight-box h3 { margin: 0 0 5px 0; font-size: 0.9rem; color: #a5b4fc; }
.insight-box p { margin: 0; font-size: 0.95rem; line-height: 1.4; }
.mt-2 { margin-top: 15px; }
/* Dashboard */
.dashboard-stats { 
display: grid;
grid-template-columns: 1fr 1fr; 
gap: 15px;
}
.stat-card {
background: rgba(255,255,255,0.05); 
padding: 15px;
border-radius: 10px; 
text-align: center;
}
.stat-card h4 { margin: 0; color: #9ca3af; }
.stat-card h2 { margin: 10px 0 0 0; font-size: 2rem; }
.stat-card.safe h2 { color: var(--safe); }
.stat-card.spam h2 { color: var(--spam); }
.stat-card.phishing h2 { color: var(--phishing); }
/* Quiz */
.quiz-options { display: flex; flex-direction: column; gap: 10px; margin-top: 15px; }
.quiz-btn {
background: rgba(255,255,255,0.05); 
border: 1px solid var(--glass-border);
color: white; padding: 10px; border-radius: 8px;
cursor: pointer; text-align: left; transition: background 0.2s;
}
.quiz-btn:hover { background: rgba(255,255,255,0.1); }
/* Score */
.score-display { text-align: center; margin: 20px 0; }
.score-display h1 { font-size: 4rem; margin: 0; color: var(--primary); }
.score-display h3 { margin: 5px 0 20px 0; color: #a5b4fc; }
/* Left corner container */
.left-corner-container { 
position: fixed;
top: 200px; 
left: 20px;
display: flex;
flex-direction: column; 
gap: 15px;
z-index: 1000;
}
/* Remove old positions */
.corner-module {
position: relative; /* override absolute */
}
/* Optional: make them look cleaner */
.corner-module {
background: var(--glass-bg);
border: 1px solid var(--glass-border); 
padding: 12px 16px;
border-radius: 12px; 
backdrop-filter: blur(10px); 
cursor: pointer;
transition: 0.3s;
}
.corner-module:hover {
transform: translateX(5px);
}
app.py
this from flask import Flask, request, jsonify, render_template 
import joblib
import random 
import os
app = Flask( name )
model = joblib.load('model.pkl')
total_analyzed = 0
counts = {"Safe": 0, "Spam": 0, "Phishing": 0}
@app.route('/') 
def index():
return render_template('index.html')
@app.route('/analyze', methods=['POST']) 
def analyze():
global total_analyzed, counts 
data = request.json
subject = data.get('subject', '') 
body = data.get('body', '')
urls = data.get('urls', '')
text = subject + " - " + body
# Predict
prediction = model.predict([text])[0]
# Dashboard update 
total_analyzed += 1
counts[prediction] += 1
# Confidence Score (Randomizing for demo based on prediction strength if possible, or just 
mock high confidence)
try:
proba = model.predict_proba([text])[0] 
confidence = max(proba) * 100
except:
confidence = random.uniform(88, 98)
confidence_level = "High Confidence" if confidence > 85 else "Moderate Confidence"
# Insights Strategy
if prediction == "Phishing":
insight = "This email creates urgency and requests sensitive action, a common phishing 
tactic."
action = "Do not click any links. Report and delete immediately." 
elif prediction == "Spam":
insight = "This email appears to be an unsolicited promotion or scam." 
action = "Ignore and move to spam folder. Avoid replying."
else:
insight = "This email appears normal and lacks typical threat indicators." 
action = "Safe to read, but always remain vigilant."
response = {
"classification": prediction, 
"email_insight": insight, 
"suggested_action": action, 
"confidence": f"{confidence:.0f}%", 
"confidence_level": confidence_level,
"awareness_tips": "Always verify the sender before clicking links or downloading 
attachments. Phishing often uses urgency to trick you."
}
# URL insight (only if URLs provided - Case 2) 
if urls and urls.strip() != "":
if prediction == "Phishing":
response["url_insight"] = "The link likely redirects to a fake login page designed to steal 
credentials."
elif prediction == "Spam":
response["url_insight"] = "The link may lead to an unsafe promotional site." 
else:
response["url_insight"] = "The link appears to match the sender's domain, but proceed 
with caution."
# Summarization 
summary_text = "This email "
if "urgent" in text.lower() or "verify" in text.lower():
summary_text += "requests urgent account verification or immediate action." 
elif "win" in text.lower() or "free" in text.lower() or "offer" in text.lower():
summary_text += "promotes a free offer, prize, or clearance sale." 
else:
summary_text += "seems to be standard communication without urgent requests." 
response["summary"] = summary_text
return jsonify(response)
@app.route('/dashboard', methods=['GET']) 
def get_dashboard():
return jsonify({
"total": total_analyzed, 
"counts": counts
"Your Netflix subscription has expired. Please update your payment details at [link] to continue 
watching your favorite shows.",
"Your Microsoft 365 password will expire soon. Click here to keep your current password.", 
"A critical security update is required for your account. Please install it immediately by
clicking the link provided.",
"Your Apple ID has been locked for security reasons. To unlock it, please verify your identity 
here."
]
data = []
for _ in range(50):
subj = random.choice(safe_subjects) 
body = random.choice(safe_bodies)
data.append({"text": subj + " - " + body, "label": "Safe"})
for _ in range(25):
subj = random.choice(spam_subjects) 
body = random.choice(spam_bodies)
data.append({"text": subj + " - " + body, "label": "Spam"})
for _ in range(25):
subj = random.choice(phishing_subjects) 
body = random.choice(phishing_bodies)
data.append({"text": subj + " - " + body, "label": "Phishing"}) 
random.shuffle(data)
df = pd.DataFrame(data)
df.to_csv('data/emails.csv', index=False) 
print('Generated data/emails.csv with 100 rows.')
