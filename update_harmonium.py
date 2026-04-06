import re

with open('d:/My Projects/web-harmoniyam-by-Atul/webharmonium.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_style = """<style>
        body {
            margin: 0;
            padding: 0;
            background: radial-gradient(circle at center, #6d4c41 0%, #3e2723 100%);
            color: #fce4ec;
            font-family: 'Georgia', serif;
        }
        .harmonium-body {
            background-color: #4e342e;
            border: 15px solid #2e1c14;
            border-radius: 10px;
            box-shadow: 0px 15px 30px rgba(0,0,0,0.8), inset 0px 5px 15px rgba(255,255,255,0.1);
            margin: 20px auto;
            padding: 20px;
            max-width: 800px;
        }
        .header-bellows {
            background: repeating-linear-gradient(
                90deg,
                #3e2723,
                #3e2723 20px,
                #271c19 20px,
                #271c19 40px
            );
            height: 60px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: inset 0px 5px 10px rgba(0,0,0,0.6);
            border: 2px solid #271c19;
        }
        .white {
            fill: url(#whiteKeyGrad);
            stroke: #9e9e9e;
            stroke-width: 1;
            cursor: pointer;
            filter: url(#dropShadow);
            transition: filter 0.1s;
        }
        .black {
            fill: url(#blackKeyGrad);
            stroke: #000;
            stroke-width: 1;
            cursor: pointer;
            filter: url(#dropShadow);
            transition: filter 0.1s;
        }
        .white:active, .white:hover, .white[data-active="true"] {
            fill: #e0e0e0;
            filter: url(#keyPressShadow);
        }
        .black:active, .black:hover, .black[data-active="true"] {
            fill: #222;
            filter: url(#keyPressShadow);
        }
        .control-panel {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            background: #5d4037;
            border: 3px solid #3e2723;
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
            box-shadow: inset 0px 3px 5px rgba(0,0,0,0.5);
        }
        .control-item {
            background: #4e342e;
            border: 2px solid #795548;
            border-radius: 10px;
            padding: 15px;
            margin: 10px;
            text-align: center;
            box-shadow: 2px 5px 10px rgba(0,0,0,0.5);
            flex: 1;
            min-width: 140px;
        }
        .control-title {
            font-size: 1.1em;
            margin-bottom: 15px;
            color: #d7ccc8;
            text-shadow: 1px 1px 2px #000;
            border-bottom: 1px solid #795548;
            padding-bottom: 5px;
        }
        .brass-knob {
            background: radial-gradient(circle, #fbc02d, #f57f17);
            border: 2px solid #bc5100;
            color: #3e2723;
            font-weight: bold;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            cursor: pointer;
            box-shadow: 2px 4px 6px rgba(0,0,0,0.6), inset 1px 2px 4px rgba(255,255,255,0.5);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            text-decoration: none;
        }
        .brass-knob:active {
            box-shadow: 1px 2px 3px rgba(0,0,0,0.6), inset 1px 2px 4px rgba(0,0,0,0.3);
            transform: translateY(2px);
        }
        .brass-display {
            background: #212121;
            color: #ffb300;
            padding: 5px 15px;
            border: 2px solid #5d4037;
            border-radius: 5px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.2em;
            display: inline-block;
            margin: 0 10px;
            box-shadow: inset 1px 2px 5px rgba(0,0,0,0.8);
            min-width: 30px;
            text-align: center;
        }
        .switch {
            position: relative;
            display: inline-block;
            width: 60px;
            height: 34px;
        }
        .switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }
        .toggle {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #3e2723;
            border: 2px solid #8d6e63;
            -webkit-transition: .4s;
            transition: .4s;
            border-radius: 34px;
            box-shadow: inset 1px 2px 5px rgba(0,0,0,0.8);
        }
        .toggle:before {
            position: absolute;
            content: "";
            height: 26px;
            width: 26px;
            left: 2px;
            bottom: 2px;
            background: radial-gradient(circle, #fbc02d, #f57f17);
            border: 1px solid #bc5100;
            -webkit-transition: .4s;
            transition: .4s;
            border-radius: 50%;
            box-shadow: 1px 2px 3px rgba(0,0,0,0.6);
        }
        input:checked + .toggle {
            background-color: #4e342e;
        }
        input:checked + .toggle:before {
            -webkit-transform: translateX(26px);
            -ms-transform: translateX(26px);
            transform: translateX(26px);
        }
        .slidecontainer {
            width: 100%;
            margin-top: 10px;
        }
        .slider {
            -webkit-appearance: none;
            width: 100%;
            height: 10px;
            background: #212121;
            outline: none;
            border-radius: 5px;
            box-shadow: inset 1px 2px 5px rgba(0,0,0,0.8);
        }
        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            background: radial-gradient(circle, #fbc02d, #f57f17);
            border: 2px solid #bc5100;
            cursor: pointer;
            box-shadow: 1px 2px 3px rgba(0,0,0,0.6);
        }
        .slider::-moz-range-thumb {
            width: 25px;
            height: 25px;
            border-radius: 50%;
            background: radial-gradient(circle, #fbc02d, #f57f17);
            border: 2px solid #bc5100;
            cursor: pointer;
            box-shadow: 1px 2px 3px rgba(0,0,0,0.6);
        }
        .title-banner {
            text-align: center;
            margin-bottom: 20px;
        }
        .title-banner h2 {
            margin: 0;
            font-family: 'Georgia', serif;
            font-style: italic;
            color: #ffecb3;
            text-shadow: 2px 2px 4px #000;
            font-size: 2.5em;
        }
        .svg-container {
            text-align: center;
            margin-bottom: 20px;
            overflow: hidden;
            padding: 20px 0;
        }
        svg {
            display: inline-block;
            transform: scale(1.6);
            transform-origin: top center;
        }
        @media screen and (max-width: 600px) {
            svg {
                transform: scale(1);
            }
        }
        .btn {
            background-color: transparent;
            border: none;
            font: inherit;
            cursor: pointer;
            padding: 0;
        }
    </style>"""

html = re.sub(r'<style>.*?</style>', new_style, html, flags=re.DOTALL)

body_start = html.find('<body>') + len('<body>')
body_end = html.rfind('</body>')

new_body_content = """
    <div class="harmonium-body">
        <div class="header-bellows"></div>
        <div class="title-banner">
            <h2>Swara Harmonium</h2>
        </div>

        <div id="load" style="text-align: center; padding: 20px;">
            <button class="brass-knob" style="width:auto; padding: 10px 20px; border-radius: 20px;" onclick="document.getElementById('load').style.display='none'; load();">Power On</button>
        </div>
        
        <div id="mainScreen" style="display: none;">
            <div class="svg-container">
                <svg width=294 height=110 id="keys-svg">
                    <defs>
                        <linearGradient id="whiteKeyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" style="stop-color:#FFFFF0;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#E8E8E8;stop-opacity:1" />
                        </linearGradient>
                        <linearGradient id="blackKeyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" style="stop-color:#4d4d4d;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#1a1a1a;stop-opacity:1" />
                        </linearGradient>
                        <filter id="dropShadow" x="-20%" y="-20%" width="140%" height="140%">
                            <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.6"/>
                        </filter>
                        <filter id="keyPressShadow" x="-20%" y="-20%" width="140%" height="140%">
                            <feDropShadow dx="0" dy="0" stdDeviation="1" flood-color="#000" flood-opacity="0.8"/>
                        </filter>
                    </defs>
"""

# Extract the polygons from the original body
polygons_match = re.search(r'(<polygon.*?</svg>)', html, flags=re.DOTALL)
if polygons_match:
    polygons = polygons_match.group(1)
    new_body_content += polygons

new_body_content += """
            </div>

            <div class="control-panel">
                <!-- Volume -->
                <div class="control-item">
                    <div class="control-title">Volume <span id="volumeLevel" style="font-size: 0.8em; color: #ffb300"></span></div>
                    <div class="slidecontainer">
                        <input type="range" min="1" max="100" value="30" class="slider" id="myRange" onchange="onGainChange()">
                    </div>
                </div>

                <!-- Reverb -->
                <div class="control-item">
                    <div class="control-title">Reverb</div>
                    <label class="switch">
                        <input id="useReverb" type="checkbox" onclick="updateReverbState(this.checked)">
                        <span class="toggle"></span>
                    </label>
                </div>

                <!-- Transpose -->
                <div class="control-item">
                    <div class="control-title">Transpose: <span id='rootNote' style="color: #ffb300">C</span></div>
                    <div>
                        <button class="brass-knob" onclick="javascript:shiftSemitone(-1)">-</button>
                        <span class="brass-display" id='transpose'>0</span>
                        <button class="brass-knob" onclick="javascript:shiftSemitone(1)">+</button>
                    </div>
                </div>

                <!-- Octave -->
                <div class="control-item">
                    <div class="control-title">Octave</div>
                    <div>
                        <button class="brass-knob" onclick="javascript:shiftOctave(-1)">-</button>
                        <span class="brass-display" id='octave'>4</span>
                        <button class="brass-knob" onclick="javascript:shiftOctave(1)">+</button>
                    </div>
                </div>

                <!-- Stack -->
                <div class="control-item">
                    <div class="control-title">Coupler / Stack</div>
                    <div>
                        <button class="brass-knob" onclick="javascript:changeStack(-1)">-</button>
                        <span class="brass-display" id='stack'>0</span>
                        <button class="brass-knob" onclick="javascript:changeStack(1)">+</button>
                    </div>
                </div>

                <!-- MIDI -->
                <div class="control-item">
                    <div class="control-title">
                        <span id="midiInputDevicesInfo" style="font-size: 0.85em">MIDI</span>
                        <button class="btn" style="color: #ffb300; margin-left: 5px" onclick="requestMIDIAccess()">
                            <i class="fa fa-refresh"></i>
                        </button>
                    </div>
                    <select id="midiInputDevices" style="width: 100%; background: #212121; color: #ffb300; border: 1px solid #bc5100; border-radius: 5px; padding: 5px;"></select>
                </div>
            </div>
        </div>
    </div>
"""

html = html[:body_start] + new_body_content + html[body_end:]

# inject data-active mapping logic to visually sink keys on keyboard hit
# find window.onkeydown = function
js_update = """
        window.onkeydown = function (event) {
            if (!event.repeat) {
                if (debug) console.log("keyDown", event.key, "keyboardMap", keyboardMap[event.key]);
                if (typeof (keyboardMap[event.key]) != "undefined") {
                    noteOn(keyboardMap[event.key]);
                    var el = document.querySelector(`polygon[key='${event.key}']`);
                    if(el) el.setAttribute('data-active', 'true');
                }
            }
        }

        window.onkeyup = function (event) {
            const key = event.key
            if (debug) console.log("keyUp", key, "keyboardMap", keyboardMap[key]);
            if (typeof (keyboardMap[key]) != "undefined") {
                noteOff(keyboardMap[key]);
                var el = document.querySelector(`polygon[key='${key}']`);
                if(el) el.removeAttribute('data-active');
            }
"""
html = re.sub(r'window\.onkeydown = function \(event\) \{.*?window\.onkeyup = function \(event\) \{.*?\}', js_update, html, flags=re.DOTALL)


with open('d:/My Projects/web-harmoniyam-by-Atul/webharmonium.html', 'w', encoding='utf-8') as f:
    f.write(html)
