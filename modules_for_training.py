# These value are highly generalized and do not reepresent the actual values in the game. They are ratios derrived from in-game experimentation and used for properly seeding the solving allgorithm.

# fmt: off
modules = {
    "standard": {
        "label": "Standard / Exotic Starships",
        "type": "Starship",
        "types": {
            "Weaponry": [
                {
                    "label": "Cyclotron Ballista",
                    "key": "cyclotron",
                    "image": "cyclotron.webp",
                    "color": "purple",
                    "modules": [
                        { "id": "CB", "type": "core", "label": "Cyclotron Ballista", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron.png", },
                        { "id": "QR", "type": "bonus", "label": "Dyson Pump", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "dyson.png", },
                        { "id": "Xa", "type": "bonus", "label": "Cyclotron Ballista Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Cyclotron Ballista Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Cyclotron Ballista Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron-upgrade.png", },
                    ],
                },
                {
                    "label": "Infraknife Accelerator",
                    "key": "infra",
                    "image": "infra.webp",
                    "color": "red",
                    "modules": [
                        { "id": "IK", "type": "core", "label": "Infraknife Accelerator", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "infra.png", },
                        { "id": "QR", "type": "bonus", "label": "Q-Resonator", "bonus": 0.00, "adjacency": "greater", "sc_eligible": True, "image": "q-resonator.png", },
                        { "id": "Xa", "type": "bonus", "label": "Infraknife Accelerator Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "infra-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Infraknife Accelerator Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "infra-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Infraknife Accelerator Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "infra-upgrade.png", },
                    ],
                },
                {
                    "label": "Phase Beam",
                    "key": "phase",
                    "image": "phase.webp",
                    "color": "green",
                    "modules": [
                        { "id": "PB", "type": "core", "label": "Phase Beam", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "phase-beam.png", },
                        { "id": "FD", "type": "bonus", "label": "Fourier De-Limiter", "bonus": 0.07, "adjacency": "lesser", "sc_eligible": True, "image": "fourier.png", },
                        { "id": "Xa", "type": "bonus", "label": "Phase Beam Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "phase-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Phase Beam Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "phase-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Phase Beam Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "phase-upgrade.png", },
                    ],
                },
                {
                    "label": "Photon Cannon",
                    "key": "photon",
                    "image": "photon.webp",
                    "color": "cyan",
                    "modules": [
                        { "id": "PC", "type": "core", "label": "Photon Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "photon.png", },
                        { "id": "NO", "type": "bonus", "label": "Nonlinear Optics", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "nonlinear.png", },
                        { "id": "Xa", "type": "bonus", "label": "Photon Cannon Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "photon-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Photon Cannon Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "photon-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Photon Cannon Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "photon-upgrade.png", },
                    ],
                },
                {
                    "label": "Positron Ejector",
                    "key": "positron",
                    "image": "positron.webp",
                    "color": "amber",
                    "modules": [
                        { "id": "PE", "type": "core", "label": "Positron Ejector", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "positron.png", },
                        { "id": "FS", "type": "bonus", "label": "Fragment Supercharger", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "fragment.png", },
                        { "id": "Xa", "type": "bonus", "label": "Positron Ejector Upgrade Theta", "bonus": 0.4, "adjacency": "greater", "sc_eligible": True, "image": "positron-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Positron Ejector Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "positron-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Positron Ejector Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "positron-upgrade.png", },
                    ],
                },
                {
                    "label": "Rocket Launcher",
                    "key": "rocket",
                    "image": "rocket.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "RL", "type": "core", "label": "Rocket Launger", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "rocket.png", },
                        { "id": "LR", "type": "bonus", "label": "Large Rocket Tubes", "bonus": 0.056, "adjacency": "greater", "sc_eligible": True, "image": "tubes.png", },
                    ],
                },
            ],
            "Defensive Systems": [
                {
                    "label": "Starship Shields",
                    "key": "shield",
                    "image": "shield.webp",
                    "color": "yellow",
                    "modules": [
                        { "id": "DS", "type": "core", "label": "Defensive Shields", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "shield.png", },
                        { "id": "AA", "type": "bonus", "label": "Ablative Armor", "bonus": 0.07, "adjacency": "greater", "sc_eligible": True, "image": "ablative.png", },
                        { "id": "Xa", "type": "bonus", "label": "Shield Upgrade Theta", "bonus": 0.3, "adjacency": "greater", "sc_eligible": True, "image": "shield-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Shield Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "shield-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Shield Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "shield-upgrade.png", },
                    ],
                },
            ],
            "Hyperdrive": [
                {
                    "label": "Hyperdrive",
                    "key": "hyper",
                    "image": "hyper.webp",
                    "color": "sky",
                    "modules": [
                        { "id": "HD", "type": "core", "label": "Hyperdrive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": False, "image": "hyperdrive.png", },
                        { "id": "AD", "type": "bonus", "label": "Atlantid Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "atlantid.png", },
                        { "id": "CD", "type": "bonus", "label": "Cadmium Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "cadmium.png", },
                        { "id": "ED", "type": "bonus", "label": "Emeril Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "emeril.png", },
                        { "id": "ID", "type": "bonus", "label": "Indium Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "indium.png", },
                        { "id": "EW", "type": "bonus", "label": "Emergency Warp Unit", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "emergency.png", },
                        { "id": "Xa", "type": "bonus", "label": "Hyperdrive Upgrade Theta", "bonus": .320, "adjacency": "greater", "sc_eligible": True, "image": "hyper-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Hyperdrive Upgrade Tau", "bonus": .310, "adjacency": "greater", "sc_eligible": True, "image": "hyper-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Hyperdrive Upgrade Sigma", "bonus": .300, "adjacency": "greater", "sc_eligible": True, "image": "hyper-upgrade.png", },
                    ],
                },
                {
                    "label": "Launch Thruster",
                    "key": "launch",
                    "image": "launch.webp",
                    "color": "jade",
                    "modules": [
                        { "id": "LT", "type": "core", "label": "Launch Thruster", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": False, "image": "launch.png", },
                        { "id": "EF", "type": "bonus", "label": "Efficient Thrusters", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "efficient.png", },
                        { "id": "RC", "type": "bonus", "label": "Launch Auto-Charger", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "recharger.png", },
                        { "id": "Xa", "type": "bonus", "label": "Launch Thruster Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "launch-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Launch Thruster Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "launch-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Launch Thruster Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "launch-upgrade.png", },
                    ],
                },
                {
                    "label": "Pulse Engine",
                    "key": "pulse",
                    "image": "pulse.webp",
                    "color": "orange",
                    "modules": [
                        { "id": "PE", "type": "core", "label": "Pulse Engine", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": False, "image": "pulse.png", },
                        { "id": "FA", "type": "bonus", "label": "Flight Assist Override", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "flight-assist.png", },
                        # { "id": "PC", "type": "reward", "label": "Photonix Core", "bonus": 0.26, "adjacency": "greater", "sc_eligible": True, "image": "photonix.png", },
                        { "id": "SL", "type": "bonus", "label": "Sub-Light Amplifier", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "sublight.png", },
                        { "id": "ID", "type": "bonus", "label": "Instability Drive", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "instability.png", },
                        { "id": "Xa", "type": "bonus", "label": "Pulse Engine Upgrade Theta", "bonus": 0.50, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Pulse Engine Upgrade Tau", "bonus": 0.49, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Pulse Engine Upgrade Sigma", "bonus": 0.48, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                    ],
                },
                {
                    "label": "Pulse Engine",
                    "key": "photonix",
                    "image": "pulse.webp",
                    "color": "orange",
                    "modules": [
                        { "id": "PE", "type": "core", "label": "Pulse Engine", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": False, "image": "pulse.png", },
                        { "id": "FA", "type": "bonus", "label": "Flight Assist Override", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "flight-assist.png", },
                        { "id": "PC", "type": "bonus", "label": "Photonix Core", "bonus": 0.26, "adjacency": "greater", "sc_eligible": True, "image": "photonix.png", },
                        { "id": "SL", "type": "bonus", "label": "Sub-Light Amplifier", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "sublight.png", },
                        { "id": "ID", "type": "bonus", "label": "Instability Drive", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "instability.png", },
                        { "id": "Xa", "type": "bonus", "label": "Pulse Engine Upgrade Theta", "bonus": 0.50, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Pulse Engine Upgrade Tau", "bonus": 0.49, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Pulse Engine Upgrade Sigma", "bonus": 0.48, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                    ],
                },
            ],
            "Utilities": [
                {
                    "label": "Aqua-Jets",
                    "key": "aqua",
                    "image": "aquajet.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AJ", "type": "core", "label": "Aqua-Jets", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "aquajets.png", },
                    ],
                },
                {
                    "label": "Figurines",
                    "key": "bobble",
                    "image": "bobble.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AP", "type": "core", "label": "Apollo Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "apollo.png", },
                        { "id": "AT", "type": "core", "label": "Atlas Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "atlas.png", },
                        { "id": "NA", "type": "bonus", "label": "Nada Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "nada.png", },
                        { "id": "NB", "type": "bonus", "label": "-null- Figurine", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "null.png", },
                    ],
                },
                {
                    "label": "Scanners",
                    "key": "scanners",
                    "image": "scanner.webp",
                    "color": "black",
                    "modules": [
                        { "id": "ES", "type": "core", "label": "Economy Scanner", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "economy.png", },
                        { "id": "CS", "type": "core", "label": "Conflict Scanner", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "conflict.png", },
                        { "id": "CD", "type": "core", "label": "Cargo Scan Deflector", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "cargo.png", },
                    ],
                },
                {
                    "label": "Starship Trails",
                    "key": "trails",
                    "image": "trails.webp",
                    "color": "gray", 
                    "modules": [
                        { "id": "AB", "type": "core", "label": "Artemis Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "artemis.png", },
                        { "id": "PB", "type": "core", "label": "Polo Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "polo.png", },
                        { "id": "SB", "type": "reward", "label": "Tentacled Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "squid.png", },
                        { "id": "SP", "type": "reward", "label": "Sputtering Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "sputtering-trail.png", },
                        { "id": "CT", "type": "bonus", "label": "Cadmium Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "cadmium-trail.png", },
                        { "id": "ET", "type": "bonus", "label": "Emeril Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "emeril-trail.png", },
                        { "id": "TT", "type": "reward", "label": "Temporal Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "temporal-trail.png", },
                        { "id": "ST", "type": "bonus", "label": "Stealth Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "stealth-trail.png", },
                        { "id": "GT", "type": "bonus", "label": "Golden Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "golden-trail.png", },
                        { "id": "RT", "type": "bonus", "label": "Chromatic Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "chromatic-trail.png", },
                    ],
                },
                {
                    "label": "Teleport Receiver",
                    "key": "teleporter",
                    "image": "teleport.webp",
                    "color": "black",
                    "modules": [
                        { "id": "TP", "type": "core", "label": "Teleport Receiver", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "teleport.png", },
                    ],
                },
            ],
        },
    },
    "sentinel": {
        "label": "Sentinel Interceptors",
        "type": "Starship",
        "types": {
            "Weaponry": [
                {
                    "label": "Cyclotron Ballista",
                    "key": "cyclotron",
                    "image": "cyclotron.webp",
                    "color": "purple",
                    "modules": [
                        { "id": "CB", "type": "core", "label": "Cyclotron Ballista", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron.png", },
                        { "id": "QR", "type": "bonus", "label": "Dyson Pump", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "dyson.png", },
                        { "id": "Xa", "type": "bonus", "label": "Cyclotron Ballista Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Cyclotron Ballista Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Cyclotron Ballista Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "cyclotron-upgrade.png", },
                    ],
                },
                {
                    "label": "Infraknife Accelerator",
                    "key": "infra",
                    "image": "infra.webp",
                    "color": "red",
                    "modules": [
                        { "id": "IK", "type": "core", "label": "Infraknife Accelerator", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "infra.png", },
                        { "id": "QR", "type": "bonus", "label": "Q-Resonator", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "q-resonator.png", },
                        { "id": "Xa", "type": "bonus", "label": "Infraknife Accelerator Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "infra-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Infraknife Accelerator Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "infra-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Infraknife Accelerator Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "infra-upgrade.png", },
                    ],
                },
                {
                    "label": "Phase Beam",
                    "key": "phase",
                    "image": "phase.webp",
                    "color": "green",
                    "modules": [
                        { "id": "PB", "type": "core", "label": "Phase Beam", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "phase-beam.png", },
                        { "id": "FD", "type": "bonus", "label": "Fourier De-Limiter", "bonus": 0.07, "adjacency": "lesser", "sc_eligible": True, "image": "fourier.png", },
                        { "id": "Xa", "type": "bonus", "label": "Phase Beam Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "phase-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Phase Beam Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "phase-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Phase Beam Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "phase-upgrade.png", },
                    ],
                },
                {
                    "label": "Positron Ejector",
                    "key": "positron",
                    "image": "positron.webp",
                    "color": "amber",
                    "modules": [
                        { "id": "PE", "type": "core", "label": "Positron Ejector", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "positron.png", },
                        { "id": "FS", "type": "bonus", "label": "Fragment Supercharger", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "fragment.png", },
                        { "id": "Xa", "type": "bonus", "label": "Positron Ejector Upgrade Theta", "bonus": 0.4, "adjacency": "greater", "sc_eligible": True, "image": "positron-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Positron Ejector Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "positron-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Positron Ejector Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "positron-upgrade.png", },
                    ],
                },
                {
                    "label": "Rocket Launcher",
                    "key": "rocket",
                    "image": "rocket.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "RL", "type": "core", "label": "Rocket Launger", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "rocket.png", },
                        { "id": "LR", "type": "bonus", "label": "Large Rocket Tubes", "bonus": 0.056, "adjacency": "greater", "sc_eligible": True, "image": "tubes.png", },
                    ],
                },
                {
                    "label": "Sentinel Cannon",
                    "key": "photon",
                    "image": "cannon.webp",
                    "color": "cyan",
                    "modules": [
                        { "id": "PC", "type": "core", "label": "Sentinel Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "cannon.png", },
                        { "id": "NO", "type": "bonus", "label": "Nonlinear Optics", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "nonlinear.png", },
                        { "id": "Xa", "type": "bonus", "label": "Photon Cannon Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "photon-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Photon Cannon Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "photon-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Photon Cannon Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "photon-upgrade.png", },
                    ],
                },
            ],
            "Defensive Systems": [
                {
                    "label": "Aeron Shields",
                    "key": "shield",
                    "image": "aeron.webp",
                    "color": "yellow",
                    "modules": [
                        { "id": "DS", "type": "core", "label": "Aeron Shields", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "aeron.png", },
                        { "id": "AA", "type": "bonus", "label": "Ablative Armor", "bonus": 0.07, "adjacency": "greater", "sc_eligible": True, "image": "ablative.png", },
                        { "id": "Xa", "type": "bonus", "label": "Shield Upgrade Theta", "bonus": 0.3, "adjacency": "greater", "sc_eligible": True, "image": "shield-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Shield Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "shield-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Shield Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "shield-upgrade.png", },
                    ],
                },
            ],
        "Hyperdrive": [
                {
                    "label": "Anti-Gravity Well",
                    "key": "launch",
                    "image": "anti-gravity.webp",
                    "color": "jade",
                    "modules": [
                        { "id": "LT", "type": "core", "label": "Anti-Gravity Well", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": False, "image": "anti-gravity.png", },
                        { "id": "EF", "type": "bonus", "label": "Efficient Thrusters", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "efficient.png", },
                        { "id": "RC", "type": "bonus", "label": "Launch Atuo-Charger", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "recharger.png", },
                        { "id": "Xa", "type": "bonus", "label": "Launch Thruster Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "launch-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Launch Thruster Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "launch-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Launch Thruster Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "launch-upgrade.png", },
                    ],
                },
                {
                    "label": "Crimson Core",
                    "key": "hyper",
                    "image": "crimson.webp",
                    "color": "sky",
                    "modules": [
                        { "id": "HD", "type": "core", "label": "Crimson Core", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": False, "image": "crimson.png", },
                        { "id": "AD", "type": "bonus", "label": "Atlantid Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "atlantid.png", },
                        { "id": "CD", "type": "bonus", "label": "Cadmium Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "cadmium.png", },
                        { "id": "ED", "type": "bonus", "label": "Emeril Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "emeril.png", },
                        { "id": "ID", "type": "bonus", "label": "Indium Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "indium.png", },
                        { "id": "EW", "type": "bonus", "label": "Emergency Warp Unit", "bonus": 0.00011, "adjacency": "greater", "sc_eligible": True, "image": "emergency.png", },
                        { "id": "Xa", "type": "bonus", "label": "Crimson Core Upgrade Theta", "bonus": 0.320, "adjacency": "greater", "sc_eligible": True, "image": "hyper-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Crimson Core Upgrade Tau", "bonus": 0.310, "adjacency": "greater", "sc_eligible": True, "image": "hyper-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Crimson Core Upgrade Sigma", "bonus": 0.300, "adjacency": "greater", "sc_eligible": True, "image": "hyper-upgrade.png", },
                  ],
                },
                {
                    "label": "Luminance Drive",
                    "key": "pulse",
                    "image": "luminance.webp",
                    "color": "orange",
                    "modules": [
                        { "id": "PE", "type": "core", "label": "Luminance Drive", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": False, "image": "luminance.png", },
                        { "id": "FA", "type": "bonus", "label": "Flight Assist Override", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "flight-assist.png", },
                        { "id": "PC", "type": "reward", "label": "Photonix Core", "bonus": 0.26, "adjacency": "greater", "sc_eligible": True, "image": "photonix.png", },
                        { "id": "SL", "type": "bonus", "label": "Sub-Light Amplifier", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "sublight.png", },
                        { "id": "ID", "type": "bonus", "label": "Instability Drive", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "instability.png", },
                        { "id": "Xa", "type": "bonus", "label": "Pulse Engine Upgrade Theta", "bonus": 0.50, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Pulse Engine Upgrade Tau", "bonus": 0.49, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Pulse Engine Upgrade Sigma", "bonus": 0.48, "adjacency": "greater", "sc_eligible": True, "image": "pulse-upgrade.png", },
                    ],
                },
            ],
            "Utilities": [
                {
                    "label": "Aqua-Jets",
                    "key": "aqua",
                    "image": "aquajet.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AJ", "type": "core", "label": "Aqua-Jets", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "aquajets.png", },
                    ],
                },
                {
                    "label": "Figurines",
                    "key": "bobble",
                    "image": "bobble.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AP", "type": "core", "label": "Apollo Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "apollo.png", },
                        { "id": "AT", "type": "core", "label": "Atlas Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "atlas.png", },
                        { "id": "NA", "type": "bonus", "label": "Nada Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "nada.png", },
                        { "id": "NB", "type": "bonus", "label": "-null- Figurine", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "null.png", },
                    ],
                },
                {
                    "label": "Pilot Interface",
                    "key": "pilot",
                    "image": "pilot.webp",
                    "color": "black",
                    "modules": [
                        { "id": "PI", "type": "bonus", "label": "Pilot Interface", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "pilot.png", },
                    ],
                },
                {
                    "label": "Scanners",
                    "key": "scanners",
                    "image": "scanner.webp",
                    "color": "black",
                    "modules": [
                        { "id": "ES", "type": "core", "label": "Economy Scanner", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "economy.png", },
                        { "id": "CS", "type": "core", "label": "Conflict Scanner", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "conflict.png", },
                        { "id": "CD", "type": "core", "label": "Cargo Scan Deflector", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "cargo.png", },
                    ],
                },
                {
                    "label": "Starship Trails",
                    "key": "trails",
                    "image": "trails.webp",
                    "color": "gray",
                    "modules": [
                        { "id": "AB", "type": "core", "label": "Artemis Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "artemis.png", },
                        { "id": "PB", "type": "core", "label": "Polo Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "polo.png", },
                        { "id": "SB", "type": "reward", "label": "Tentacled Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "squid.png", },
                        { "id": "SP", "type": "reward", "label": "Sputtering Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "sputtering-trail.png", },
                        { "id": "CT", "type": "bonus", "label": "Cadmium Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "cadmium-trail.png", },
                        { "id": "ET", "type": "bonus", "label": "Emeril Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "emeril-trail.png", },
                        { "id": "TT", "type": "reward", "label": "Temporal Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "temporal-trail.png", },
                        { "id": "ST", "type": "bonus", "label": "Stealth Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "stealth-trail.png", },
                        { "id": "GT", "type": "bonus", "label": "Golden Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "golden-trail.png", },
                        { "id": "RT", "type": "bonus", "label": "Chromatic Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "chromatic-trail.png", },
                     ],
                },
                {
                    "label": "Teleport Receiver",
                    "key": "teleporter",
                    "image": "teleport.webp",
                    "color": "black",
                    "modules": [
                        { "id": "TP", "type": "core", "label": "Teleport Receiver", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "teleport.png", },
                    ],
                },
            ],
        },
    },
    "living": {
        "label": "Living Starships",
        "type": "Starship",
        "types": {
            "Weaponry": [
                {
                    "label": "Grafted Eyes",
                    "key": "grafted",
                    "image": "grafted.webp",
                    "color": "green",
                    "modules": [
                        { "id": "GE", "type": "core", "label": "Grafted Eyes", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "grafted.png", },
                        { "id": "Xa", "type": "bonus", "label": "Grafted Eyes Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "grafted-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Grafted Eyes Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "grafted-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Grafted Eyes Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "grafted-upgrade.png", },
                    ],
                },
                {
                    "label": "Spewing Vents",
                    "key": "spewing",
                    "image": "spewing.webp",
                    "color": "cyan",
                    "modules": [
                        { "id": "SV", "type": "core", "label": "Spewing Vents", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "spewing.png", },
                        { "id": "Xa", "type": "bonus", "label": "Spewing Vents Upgrade Theta", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "spewing-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Spewing Vents Upgrade Tau", "bonus": 0.39, "adjacency": "greater", "sc_eligible": True, "image": "spewing-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Spewing Vents Upgrade Sigma", "bonus": 0.38, "adjacency": "greater", "sc_eligible": True, "image": "spewing-upgrade.png", },
                    ],
                },
            ],
            "Defensive Systems": [
                {
                    "label": "Scream Supressor",
                    "key": "scream",
                    "image": "scream.webp",
                    "color": "yellow",
                    "modules": [
                        { "id": "SS", "type": "core", "label": "Scream Supressor", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "scream.png", },
                        { "id": "Xa", "type": "bonus", "label": "Scream Supressor Upgrade Theta", "bonus": 0.3, "adjacency": "greater", "sc_eligible": True, "image": "scream-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Scream Supressor Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "scream-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Scream Supressor Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "scream-upgrade.png", },
                    ],
                },
            ],
            "Hyperdrive": [
                {
                    "label": "Neural Assembly",
                    "key": "assembly",
                    "image": "assembly.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "NA", "type": "core", "label": "Neural Assembly", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "assembly.png", },
                        { "id": "Xa", "type": "bonus", "label": "Neural Assembly Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "assembly-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Neural Assembly Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "assembly-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Neural Assembly Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "assembly-upgrade.png", },
                        { "id": "CM", "type": "bonus", "label": "Chroloplast Membrane", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "chloroplast.png", },
                    ],
                },
                {
                    "label": "Singularity Cortex",
                    "key": "singularity",
                    "image": "singularity.webp",
                    "color": "sky",
                    "modules": [
                        { "id": "SC", "type": "core", "label": "Singularity Cortex", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "singularity.png", },
                        { "id": "AD", "type": "bonus", "label": "Atlantid Drive", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "atlantid.png", },
                        { "id": "Xa", "type": "bonus", "label": "Singularity Cortex Upgrade Theta", "bonus": 0.320, "adjacency": "greater", "sc_eligible": True, "image": "singularity-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Singularity Cortex Upgrade Tau", "bonus": 0.310, "adjacency": "greater", "sc_eligible": True, "image": "singularity-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Singularity Cortex Upgrade Sigma", "bonus": 0.300, "adjacency": "greater", "sc_eligible": True, "image": "singularity-upgrade.png", },
                    ],
                },
                {
                    "label": "Pulsing Heart",
                    "key": "pulsing",
                    "image": "pulsing.webp",
                    "color": "orange",
                    "modules": [
                        { "id": "PH", "type": "core", "label": "Pulsing Heart", "bonus": 0.0001, "adjacency": "lesser", "sc_eligible": True, "image": "pulsing.png", },
                        { "id": "Xa", "type": "bonus", "label": "Pulsing Heart Upgrade Theta", "bonus": 0.50, "adjacency": "greater", "sc_eligible": True, "image": "pulsing-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Pulsing Heart Upgrade Tau", "bonus": 0.49, "adjacency": "greater", "sc_eligible": True, "image": "pulsing-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Pulsing Heart Upgrade Sigma", "bonus": 0.48, "adjacency": "greater", "sc_eligible": True, "image": "pulsing-upgrade.png", },
                    ],
                },
            ],
            "Utilities": [
                {
                    "label": "Saline Carapace",
                    "key": "saline",
                    "image": "saline.webp",
                    "color": "black",
                    "modules": [
                        { "id": "SC", "type": "core", "label": "Saline Catapace", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "saline.png", },
                    ],
                },
                {
                    "label": "Figurines",
                    "key": "bobble",
                    "image": "bobble.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AP", "type": "core", "label": "Apollo Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "apollo.png", },
                        { "id": "AT", "type": "core", "label": "Atlas Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "atlas.png", },
                        { "id": "NA", "type": "bonus", "label": "Nada Figurine", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "nada.png", },
                        { "id": "NB", "type": "bonus", "label": "-null- Figurine", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "null.png", },
                    ],
                },
                {
                    "label": "Scanners",
                    "key": "scanners",
                    "image": "wormhole.webp",
                    "color": "black",
                    "modules": [
                        { "id": "WB", "type": "core", "label": "Wormhole Brain", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "wormhole.png", },
                        { "id": "NS", "type": "core", "label": "Neural Shielding", "bonus": 0.0, "adjacency": "none", "sc_eligible": False, "image": "neural.png", },
                    ],
                },
                {
                    "label": "Starship Trails",
                    "key": "trails",
                    "image": "trails.webp",
                    "color": "gray",
                    "modules": [
                        { "id": "AB", "type": "core", "label": "Artemis Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "artemis.png", },
                        { "id": "PB", "type": "core", "label": "Polo Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "polo.png", },
                        { "id": "SB", "type": "reward", "label": "Tentacled Figurine", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "squid.png", },
                        { "id": "SP", "type": "reward", "label": "Sputtering Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "sputtering-trail.png", },
                        { "id": "CT", "type": "bonus", "label": "Cadmium Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "cadmium-trail.png", },
                        { "id": "ET", "type": "bonus", "label": "Emeril Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "emeril-trail.png", },
                        { "id": "TT", "type": "reward", "label": "Temporal Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "temporal-trail.png", },
                        { "id": "ST", "type": "bonus", "label": "Stealth Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "stealth-trail.png", },
                        { "id": "GT", "type": "bonus", "label": "Golden Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "golden-trail.png", },
                        { "id": "RT", "type": "bonus", "label": "Chromatic Starship Trail", "bonus": 0.01, "adjacency": "greater", "sc_eligible": True, "image": "chromatic-trail.png", },
                    ],
                },
            ],
        },
    },
    "standard-mt": {
        "label": "Standard / Exotic Multi-Tools",
        "type": "Multi-Tool",
        "types": {
            "Mining": [
                {
                    "label": "Mining Beam",
                    "key": "mining",
                    "image": "mining-beam.webp",
                    "color": "green",
                    "modules": [
                        { "id": "MB", "type": "core", "label": "Mining Laser", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "mining-laser.png", },
                        { "id": "AM", "type": "bonus", "label": "Advanced Mining Laser", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "advanced-mining.png", },
                        { "id": "OD", "type": "bonus", "label": "Optical Drill", "bonus": 0.50, "adjacency": "greater", "sc_eligible": True, "image": "optical.png", },
                        { "id": "Xa", "type": "bonus", "label": "Mining Laser Upgrade Theta", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Mining Laser Upgrade Tau", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Mining Laser Upgrade Sigma", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                    ],
                },
            ],
            "Scanners": [
                {
                    "label": "Analysis Visor",
                    "key": "analysis",
                    "image": "analysis.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AV", "type": "core", "label": "Paralysis Mortar", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "analysis.png", },
                    ],
                },
                {
                    "label": "Scanner",
                    "key": "scanner",
                    "image": "mt-scanner.webp",
                    "color": "yellow",
                    "modules": [
                        { "id": "SC", "type": "core", "label": "Scanner", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "mt-scanner.png", },
                        { "id": "WR", "type": "bonus", "label": "Waveform Recycler", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "waveform.png", },
                        { "id": "SH", "type": "bonus", "label": "Scan Harmonizer", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "harmonizer.png", },
                        { "id": "PC", "type": "bonus", "label": "Polyphonic Core", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "polyphonic.png", },
                        { "id": "Xa", "type": "bonus", "label": "Scanner Upgrade Theta", "bonus": 1.50, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Scanner Upgrade Tau", "bonus": 1.45, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Scanner Upgrade Sigma", "bonus": 1.40, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                    ],
                },
                {
                    "label": "Survey Device",
                    "key": "survey",
                    "image": "survey.webp",
                    "color": "black",
                    "modules": [
                        { "id": "SD", "type": "core", "label": "Survey Device", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "survey.png", },
                    ],
                },
            ],
            "Weaponry": [
                {
                    "label": "Blaze Javelin",
                    "key": "blaze-javelin",
                    "image": "blaze-javelin.webp",
                    "color": "red",
                    "modules": [
                        { "id": "BJ", "type": "core", "label": "Blaze Javelin", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "blaze-javelin.png", },
                        { "id": "MA", "type": "bonus", "label": "Mass Accelerator", "bonus": .20, "adjacency": "greater", "sc_eligible": True, "image": "mass-accelerator.png", },
                        { "id": "WO", "type": "bonus", "label": "Waveform Oscillator", "bonus": 0.0, "adjacency": "none", "sc_eligible": True, "image": "waveform-osc.png", },               
                        { "id": "Xa", "type": "bonus", "label": "Blaze Javelin Upgrade Theta", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Blaze Javelin Upgrade Tau", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Blaze Javelin Upgrade Sigma", "bonus": 0.03, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                    ],
                },
                {
                    "label": "Boltcaster",
                    "key": "bolt-caster",
                    "image": "boltcaster.webp",
                    "color": "cyan",
                    "modules": [
                        { "id": "BC", "type": "core", "label": "Bolt Caster", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "boltcaster.png", },
                        { "id": "RM", "type": "bonus", "label": "Boltcaster Ricochet Module", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-rm.png", },
                        { "id": "BI", "type": "bonus", "label": "Barrel Ionizer", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "barrel-ionizer.png", },               
                        { "id": "Xa", "type": "bonus", "label": "Boltcaster Upgrade Theta", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Boltcaster Upgrade Tau", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Boltcaster Upgrade Sigma", "bonus": 0.03, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                    ],
                },
                {
                    "label": "Geology Cannon",
                    "key": "geology",
                    "image": "geology.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "GC", "type": "core", "label": "Geology Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "geology.png", },
                        { "id": "Xa", "type": "bonus", "label": "Geology Cannon Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Geology Cannon Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Geology Cannon Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                    ],
                },
                {
                    "label": "Neutron Cannon",
                    "key": "neutron",
                    "image": "neutron.webp",
                    "color": "purple",
                    "modules": [
                        { "id": "NC", "type": "core", "label": "Neutron Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "neutron.png", },
                        { "id": "PF", "type": "bonus", "label": "P-Field Compressor", "bonus": 0.5, "adjacency": "greater", "sc_eligible": True, "image": "p-field.png", },
                        { "id": "Xa", "type": "bonus", "label": "Neutron Cannon Upgrade Theta", "bonus": 1.70, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Neutron Cannon Upgrade Tau", "bonus": 1.60, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Neutron Cannon Upgrade Sigma", "bonus": 1.50, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                    ],
                },
                {
                    "label": "Plasma Launcher",
                    "key": "plasma-launcher",
                    "image": "plasma-launcher.webp",
                    "color": "sky",
                    "modules": [
                        { "id": "PL", "type": "core", "label": "Plasma Launcher", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "plasma-launcher.png", },
                        { "id": "Xa", "type": "bonus", "label": "Plasma Launcher Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Plasma Launcher Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Plasma Launcher Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                    ],
                },
                {
                    "label": "Pulse Splitter",
                    "key": "pulse-splitter",
                    "image": "pulse-splitter.webp",
                    "color": "jade",
                    "modules": [
                        { "id": "PS", "type": "core", "label": "Pulse Splitter", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter.png", },
                        { "id": "AC", "type": "bonus", "label": "Amplified Cartridges", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "amplified.png", },
                        { "id": "RM", "type": "bonus", "label": "Richochet Module", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-rm.png", },
                        { "id": "II", "type": "bonus", "label": "Impact Ignitor", "bonus": 0.0, "adjacency": "none", "sc_eligible": True, "image": "impact-ignitor.png", },
                        { "id": "Xa", "type": "bonus", "label": "Pulse Splitter Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Pulse Splitter Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Pulse Splitter Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                    ],
                },
                {
                    "label": "Scatter Blaster",
                    "key": "scatter",
                    "image": "scatter.webp",
                    "color": "amber",
                    "modules": [
                        { "id": "SB", "type": "core", "label": "Scatter Blaster", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "scatter.png", },
                        { "id": "SG", "type": "bonus", "label": "Shell Greaser", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "shell-greaser.png", },
                        { "id": "Xa", "type": "bonus", "label": "Scatter Blaster Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Scatter Blaster Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Scatter Blaster Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                    ],
                },
            ],
            "Secondary Weapons": [
                {
                    "label": "Cloaking Device",
                    "key": "cloaking",
                    "image": "cloaking.webp",
                    "color": "black",
                    "modules": [
                        { "id": "CD", "type": "core", "label": "Cloaking Device", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "cloaking.png", },
                    ],
                },
                {
                    "label": "Combat Scope",
                    "key": "combat",
                    "image": "combat.webp",
                    "color": "black",
                    "modules": [
                        { "id": "CS", "type": "core", "label": "Combat Scope", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "combat.png", },
                    ],
                },
                {
                    "label": "Voltaic Amplifier",
                    "key": "voltaic-amplifier",
                    "image": "voltaic-amplifier.webp",
                    "color": "black",
                    "modules": [
                        { "id": "VA", "type": "core", "label": "Voltaic Amplifier", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "voltaic-amplifier.png", },
                    ],
                },
                {
                    "label": "Paralysis Mortar",
                    "key": "paralysis",
                    "image": "paralysis.webp",
                    "color": "black",
                    "modules": [
                        { "id": "PM", "type": "core", "label": "Paralysis Mortar", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "paralysis.png", },
                    ],
                },
                {
                    "label": "Personal Forcefield",
                    "key": "personal",
                    "image": "personal.webp",
                    "color": "black",
                    "modules": [
                        { "id": "PF", "type": "core", "label": "Personal Forcefield", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "personal.png", },
                    ],
                },
            ],
            "Utilities": [
                {
                    "label": "Fishing Rig",
                    "key": "fishing",
                    "image": "fishing.webp",
                    "color": "black",
                    "modules": [
                        { "id": "FR", "type": "core", "label": "F", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "fishing.png", },
                    ],
                },
                {
                    "label": "Forbidden Modules",
                    "key": "forbidden",
                    "image": "forbidden.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "Fa", "type": "core", "label": "Forbidden Module Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                        { "id": "Fb", "type": "core", "label": "Forbidden Module Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                        { "id": "Fc", "type": "core", "label": "Forbidden Module Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                    ],
                },
                {
                    "label": "Terrain Manipulator",
                    "key": "terrian",
                    "image": "terrian.webp",
                    "color": "black",
                    "modules": [
                        { "id": "TM", "type": "core", "label": "Fishing Rig", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "terrian.png", },
                    ],
                },
            ],
        },
    },
    "atlantid": {
        "label": "Atlantid Multi-Tools",
        "type": "Multi-Tool",
        "types": {
            "Mining": [
                {
                    "label": "Mining Beam",
                    "key": "mining",
                    "image": "mining-beam.webp",
                    "color": "green",
                    "modules": [
                        { "id": "MB", "type": "core", "label": "Mining Laser", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "mining-laser.png", },
                        { "id": "AM", "type": "bonus", "label": "Advanced Mining Laser", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "advanced-mining.png", },
                        { "id": "OD", "type": "bonus", "label": "Optical Drill", "bonus": 0.50, "adjacency": "greater", "sc_eligible": True, "image": "optical.png", },
                        { "id": "Xa", "type": "bonus", "label": "Mining Laser Upgrade Theta", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Mining Laser Upgrade Tau", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Mining Laser Upgrade Sigma", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                        { "id": "RL", "type": "bonus", "label": "Runic Laser", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "runic-laser.png", },
                    ],
                },
            ],
            "Scanners": [
                {
                    "label": "Analysis Visor",
                    "key": "analysis",
                    "image": "analysis.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AV", "type": "core", "label": "Paralysis Mortar", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "analysis.png", },
                    ],
                },
                {
                    "label": "Scanner",
                    "key": "scanner",
                    "image": "mt-scanner.webp",
                    "color": "yellow",
                    "modules": [
                        { "id": "SC", "type": "core", "label": "Scanner", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "mt-scanner.png", },
                        { "id": "WR", "type": "bonus", "label": "Waveform Recycler", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "waveform.png", },
                        { "id": "SH", "type": "bonus", "label": "Scan Harmonizer", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "harmonizer.png", },
                        { "id": "PC", "type": "bonus", "label": "Polyphonic Core", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "polyphonic.png", },
                        { "id": "Xa", "type": "bonus", "label": "Scanner Upgrade Theta", "bonus": 1.50, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Scanner Upgrade Tau", "bonus": 1.45, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Scanner Upgrade Sigma", "bonus": 1.40, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                    ],
                },
                {
                    "label": "Survey Device",
                    "key": "survey",
                    "image": "survey.webp",
                    "color": "black",
                    "modules": [
                        { "id": "SD", "type": "core", "label": "Survey Device", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "survey.png", },
                    ],
                },
            ],
            "Weaponry": [
                {
                    "label": "Blaze Javelin",
                    "key": "blaze-javelin",
                    "image": "blaze-javelin.webp",
                    "color": "red",
                    "modules": [
                        { "id": "BJ", "type": "core", "label": "Blaze Javelin", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "blaze-javelin.png", },
                        { "id": "MA", "type": "bonus", "label": "Mass Accelerator", "bonus": .20, "adjacency": "greater", "sc_eligible": True, "image": "mass-accelerator.png", },
                        { "id": "WO", "type": "bonus", "label": "Waveform Oscillator", "bonus": 0.0, "adjacency": "none", "sc_eligible": True, "image": "waveform-osc.png", },               
                        { "id": "Xa", "type": "bonus", "label": "Blaze Javelin Upgrade Theta", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Blaze Javelin Upgrade Tau", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Blaze Javelin Upgrade Sigma", "bonus": 0.03, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                    ],
                },
                {
                    "label": "Boltcaster",
                    "key": "bolt-caster",
                    "image": "boltcaster.webp",
                    "color": "cyan",
                    "modules": [
                        { "id": "BC", "type": "core", "label": "Bolt Caster", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "boltcaster.png", },
                        { "id": "RM", "type": "bonus", "label": "Boltcaster Ricochet Module", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-rm.png", },
                        { "id": "BI", "type": "bonus", "label": "Barrel Ionizer", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "barrel-ionizer.png", },               
                        { "id": "Xa", "type": "bonus", "label": "Boltcaster Upgrade Theta", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Boltcaster Upgrade Tau", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Boltcaster Upgrade Sigma", "bonus": 0.03, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                    ],
                },
                {
                    "label": "Geology Cannon",
                    "key": "geology",
                    "image": "geology.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "GC", "type": "core", "label": "Geology Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "geology.png", },
                        { "id": "Xa", "type": "bonus", "label": "Geology Cannon Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Geology Cannon Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Geology Cannon Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                    ],
                },
                {
                    "label": "Neutron Cannon",
                    "key": "neutron",
                    "image": "neutron.webp",
                    "color": "purple",
                    "modules": [
                        { "id": "NC", "type": "core", "label": "Neutron Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "neutron.png", },
                        { "id": "PF", "type": "bonus", "label": "P-Field Compressor", "bonus": 0.5, "adjacency": "greater", "sc_eligible": True, "image": "p-field.png", },
                        { "id": "Xa", "type": "bonus", "label": "Neutron Cannon Upgrade Theta", "bonus": 1.70, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Neutron Cannon Upgrade Tau", "bonus": 1.60, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Neutron Cannon Upgrade Sigma", "bonus": 1.50, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                    ],
                },
                {
                    "label": "Plasma Launcher",
                    "key": "plasma-launcher",
                    "image": "plasma-launcher.webp",
                    "color": "sky",
                    "modules": [
                        { "id": "PL", "type": "core", "label": "Plasma Launcher", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "plasma-launcher.png", },
                        { "id": "Xa", "type": "bonus", "label": "Plasma Launcher Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Plasma Launcher Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Plasma Launcher Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                    ],
                },
                {
                    "label": "Pulse Splitter",
                    "key": "pulse-splitter",
                    "image": "pulse-splitter.webp",
                    "color": "jade",
                    "modules": [
                        { "id": "PS", "type": "core", "label": "Pulse Splitter", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter.png", },
                        { "id": "AC", "type": "bonus", "label": "Amplified Cartridges", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "amplified.png", },
                        { "id": "RM", "type": "bonus", "label": "Richochet Module", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-rm.png", },
                        { "id": "II", "type": "bonus", "label": "Impact Ignitor", "bonus": 0.0, "adjacency": "none", "sc_eligible": True, "image": "impact-ignitor.png", },
                        { "id": "Xa", "type": "bonus", "label": "Pulse Splitter Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Pulse Splitter Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Pulse Splitter Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                    ],
                },
                {
                    "label": "Scatter Blaster",
                    "key": "scatter",
                    "image": "scatter.webp",
                    "color": "amber",
                    "modules": [
                        { "id": "SB", "type": "core", "label": "Scatter Blaster", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "scatter.png", },
                        { "id": "SG", "type": "bonus", "label": "Shell Greaser", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "shell-greaser.png", },
                        { "id": "Xa", "type": "bonus", "label": "Scatter Blaster Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Scatter Blaster Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Scatter Blaster Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                    ],
                },
            ],
            "Secondary Weapons": [
                {
                    "label": "Cloaking Device",
                    "key": "cloaking",
                    "image": "cloaking.webp",
                    "color": "black",
                    "modules": [
                        { "id": "CD", "type": "core", "label": "Cloaking Device", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "cloaking.png", },
                    ],
                },
                {
                    "label": "Combat Scope",
                    "key": "combat",
                    "image": "combat.webp",
                    "color": "black",
                    "modules": [
                        { "id": "CS", "type": "core", "label": "Combat Scope", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "combat.png", },
                    ],
                },
                {
                    "label": "Voltaic Amplifier",
                    "key": "voltaic-amplifier",
                    "image": "voltaic-amplifier.webp",
                    "color": "black",
                    "modules": [
                        { "id": "VA", "type": "core", "label": "Voltaic Amplifier", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "voltaic-amplifier.png", },
                    ],
                },
                {
                    "label": "Paralysis Mortar",
                    "key": "paralysis",
                    "image": "paralysis.webp",
                    "color": "black",
                    "modules": [
                        { "id": "PM", "type": "core", "label": "Paralysis Mortar", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "paralysis.png", },
                    ],
                },
                {
                    "label": "Personal Forcefield",
                    "key": "personal",
                    "image": "personal.webp",
                    "color": "black",
                    "modules": [
                        { "id": "PF", "type": "core", "label": "Personal Forcefield", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "personal.png", },
                    ],
                },
            ],
            "Utilities": [
                {
                    "label": "Fishing Rig",
                    "key": "fishing",
                    "image": "fishing.webp",
                    "color": "black",
                    "modules": [
                        { "id": "FR", "type": "core", "label": "F", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "fishing.png", },
                    ],
                },
                {
                    "label": "Forbidden Modules",
                    "key": "forbidden",
                    "image": "forbidden.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "Fa", "type": "core", "label": "Forbidden Module Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                        { "id": "Fb", "type": "core", "label": "Forbidden Module Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                        { "id": "Fc", "type": "core", "label": "Forbidden Module Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                    ],
                },
                {
                    "label": "Terrain Manipulator",
                    "key": "terrian",
                    "image": "terrian.webp",
                    "color": "black",
                    "modules": [
                        { "id": "TM", "type": "core", "label": "Fishing Rig", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "terrian.png", },
                    ],
                },
            ],
        },
    }, 
    "sentinel-mt": {
        "label": "Sentinel Multi-Tools",
        "type": "Multi-Tool",
        "types": {
            "Mining": [
                {
                    "label": "Hijacked Laser",
                    "key": "mining",
                    "image": "hijacked.webp",
                    "color": "green",
                    "modules": [
                        { "id": "MB", "type": "core", "label": "Hijacked Laser", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "hijacked.png", },
                        { "id": "AM", "type": "bonus", "label": "Advanced Mining Laser", "bonus": 0.40, "adjacency": "greater", "sc_eligible": True, "image": "advanced-mining.png", },
                        { "id": "OD", "type": "bonus", "label": "Optical Drill", "bonus": 0.50, "adjacency": "greater", "sc_eligible": True, "image": "optical.png", },
                        { "id": "Xa", "type": "bonus", "label": "Mining Laser Upgrade Theta", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Mining Laser Upgrade Tau", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Mining Laser Upgrade Sigma", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "mining-upgrade.png", },
                    ],
                },
            ],
            "Scanners": [
                {
                    "label": "Analysis Visor",
                    "key": "analysis",
                    "image": "analysis.webp",
                    "color": "black",
                    "modules": [
                        { "id": "AV", "type": "core", "label": "Paralysis Mortar", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "analysis.png", },
                    ],
                },
                {
                    "label": "Scanner",
                    "key": "scanner",
                    "image": "mt-scanner.webp",
                    "color": "yellow",
                    "modules": [
                        { "id": "SC", "type": "core", "label": "Scanner", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "mt-scanner.png", },
                        { "id": "WR", "type": "bonus", "label": "Waveform Recycler", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "waveform.png", },
                        { "id": "SH", "type": "bonus", "label": "Scan Harmonizer", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "harmonizer.png", },
                        { "id": "PC", "type": "bonus", "label": "Polyphonic Core", "bonus": 0.11, "adjacency": "greater", "sc_eligible": True, "image": "polyphonic.png", },
                        { "id": "Xa", "type": "bonus", "label": "Scanner Upgrade Theta", "bonus": 1.50, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Scanner Upgrade Tau", "bonus": 1.45, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Scanner Upgrade Sigma", "bonus": 1.40, "adjacency": "greater", "sc_eligible": True, "image": "scanner-upgrade.png", },
                    ],
                },
                {
                    "label": "Survey Device",
                    "key": "survey",
                    "image": "survey.webp",
                    "color": "black",
                    "modules": [
                        { "id": "SD", "type": "core", "label": "Survey Device", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "survey.png", },
                    ],
                },
            ],
            "Weaponry": [
                {
                    "label": "Blaze Javelin",
                    "key": "blaze-javelin",
                    "image": "blaze-javelin.webp",
                    "color": "red",
                    "modules": [
                        { "id": "BJ", "type": "core", "label": "Blaze Javelin", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "blaze-javelin.png", },
                        { "id": "MA", "type": "bonus", "label": "Mass Accelerator", "bonus": .20, "adjacency": "greater", "sc_eligible": True, "image": "mass-accelerator.png", },
                        { "id": "WO", "type": "bonus", "label": "Waveform Oscillator", "bonus": 0.0, "adjacency": "none", "sc_eligible": True, "image": "waveform-osc.png", },               
                        { "id": "Xa", "type": "bonus", "label": "Blaze Javelin Upgrade Theta", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Blaze Javelin Upgrade Tau", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Blaze Javelin Upgrade Sigma", "bonus": 0.03, "adjacency": "greater", "sc_eligible": True, "image": "blaze-upgrade.png", },
                    ],
                },
                {
                    "label": "Boltcaster",
                    "key": "bolt-caster",
                    "image": "boltcaster.webp",
                    "color": "cyan",
                    "modules": [
                        { "id": "BC", "type": "core", "label": "Bolt Caster", "bonus": 1.0, "adjacency": "lesser", "sc_eligible": True, "image": "boltcaster.png", },
                        { "id": "RM", "type": "bonus", "label": "Boltcaster Ricochet Module", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-rm.png", },
                        { "id": "BI", "type": "bonus", "label": "Barrel Ionizer", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "barrel-ionizer.png", },               
                        { "id": "Xa", "type": "bonus", "label": "Boltcaster Upgrade Theta", "bonus": 0.05, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Boltcaster Upgrade Tau", "bonus": 0.04, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Boltcaster Upgrade Sigma", "bonus": 0.03, "adjacency": "greater", "sc_eligible": True, "image": "boltcaster-upgrade.png", },
                    ],
                },
                {
                    "label": "Geology Cannon",
                    "key": "geology",
                    "image": "geology.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "GC", "type": "core", "label": "Geology Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "geology.png", },
                        { "id": "Xa", "type": "bonus", "label": "Geology Cannon Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Geology Cannon Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Geology Cannon Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "geology-upgrade.png", },
                    ],
                },
                {
                    "label": "Neutron Cannon",
                    "key": "neutron",
                    "image": "neutron.webp",
                    "color": "purple",
                    "modules": [
                        { "id": "NC", "type": "core", "label": "Neutron Cannon", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "neutron.png", },
                        { "id": "PF", "type": "bonus", "label": "P-Field Compressor", "bonus": 0.5, "adjacency": "greater", "sc_eligible": True, "image": "p-field.png", },
                        { "id": "Xa", "type": "bonus", "label": "Neutron Cannon Upgrade Theta", "bonus": 1.70, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Neutron Cannon Upgrade Tau", "bonus": 1.60, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Neutron Cannon Upgrade Sigma", "bonus": 1.50, "adjacency": "greater", "sc_eligible": True, "image": "neutron-upgrade.png", },
                    ],
                },
                {
                    "label": "Plasma Launcher",
                    "key": "plasma-launcher",
                    "image": "plasma-launcher.webp",
                    "color": "sky",
                    "modules": [
                        { "id": "PL", "type": "core", "label": "Plasma Launcher", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "plasma-launcher.png", },
                        { "id": "Xa", "type": "bonus", "label": "Plasma Launcher Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Plasma Launcher Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Plasma Launcher Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "plasma-upgrade.png", },
                    ],
                },
                {
                    "label": "Pulse Splitter",
                    "key": "pulse-splitter",
                    "image": "pulse-splitter.webp",
                    "color": "jade",
                    "modules": [
                        { "id": "PS", "type": "core", "label": "Pulse Splitter", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter.png", },
                        { "id": "AC", "type": "bonus", "label": "Amplified Cartridges", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "amplified.png", },
                        { "id": "RM", "type": "bonus", "label": "Richochet Module", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-rm.png", },
                        { "id": "II", "type": "bonus", "label": "Impact Ignitor", "bonus": 0.0, "adjacency": "none", "sc_eligible": True, "image": "impact-ignitor.png", },
                        { "id": "Xa", "type": "bonus", "label": "Pulse Splitter Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Pulse Splitter Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Pulse Splitter Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "pulse-splitter-upgrade.png", },
                    ],
                },
                {
                    "label": "Scatter Blaster",
                    "key": "scatter",
                    "image": "scatter.webp",
                    "color": "amber",
                    "modules": [
                        { "id": "SB", "type": "core", "label": "Scatter Blaster", "bonus": 1.0, "adjacency": "greater", "sc_eligible": True, "image": "scatter.png", },
                        { "id": "SG", "type": "bonus", "label": "Shell Greaser", "bonus": 0.0001, "adjacency": "greater", "sc_eligible": True, "image": "shell-greaser.png", },
                        { "id": "Xa", "type": "bonus", "label": "Scatter Blaster Upgrade Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                        { "id": "Xb", "type": "bonus", "label": "Scatter Blaster Upgrade Tau", "bonus": 0.29, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                        { "id": "Xc", "type": "bonus", "label": "Scatter Blaster Upgrade Sigma", "bonus": 0.28, "adjacency": "greater", "sc_eligible": True, "image": "scatter-upgrade.png", },
                    ],
                },
            ],
            "Secondary Weapons": [
                {
                    "label": "Cloaking Device",
                    "key": "cloaking",
                    "image": "cloaking.webp",
                    "color": "black",
                    "modules": [
                        { "id": "CD", "type": "core", "label": "Cloaking Device", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "cloaking.png", },
                    ],
                },
                {
                    "label": "Combat Scope",
                    "key": "combat",
                    "image": "combat.webp",
                    "color": "black",
                    "modules": [
                        { "id": "CS", "type": "core", "label": "Combat Scope", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "combat.png", },
                    ],
                },
                {
                    "label": "Voltaic Amplifier",
                    "key": "voltaic-amplifier",
                    "image": "voltaic-amplifier.webp",
                    "color": "black",
                    "modules": [
                        { "id": "VA", "type": "core", "label": "Voltaic Amplifier", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "voltaic-amplifier.png", },
                    ],
                },
                {
                    "label": "Paralysis Mortar",
                    "key": "paralysis",
                    "image": "paralysis.webp",
                    "color": "black",
                    "modules": [
                        { "id": "PM", "type": "core", "label": "Paralysis Mortar", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "paralysis.png", },
                    ],
                },
                {
                    "label": "Personal Forcefield",
                    "key": "personal",
                    "image": "personal.webp",
                    "color": "black",
                    "modules": [
                        { "id": "PF", "type": "core", "label": "Personal Forcefield", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "personal.png", },
                    ],
                },
            ],
            "Utilities": [
                {
                    "label": "Fishing Rig",
                    "key": "fishing",
                    "image": "fishing.webp",
                    "color": "black",
                    "modules": [
                        { "id": "FR", "type": "core", "label": "F", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "fishing.png", },
                    ],
                },
                {
                    "label": "Forbidden Modules",
                    "key": "forbidden",
                    "image": "forbidden.webp",
                    "color": "iris",
                    "modules": [
                        { "id": "Fa", "type": "core", "label": "Forbidden Module Theta", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                        { "id": "Fb", "type": "core", "label": "Forbidden Module Tau", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                        { "id": "Fc", "type": "core", "label": "Forbidden Module Sigma", "bonus": 0.30, "adjacency": "greater", "sc_eligible": True, "image": "forbidden.png", },
                    ],
                },
                {
                    "label": "Terrain Manipulator",
                    "key": "terrian",
                    "image": "terrian.webp",
                    "color": "black",
                    "modules": [
                        { "id": "TM", "type": "core", "label": "Fishing Rig", "bonus": 0.0, "adjacency": "greater", "sc_eligible": False, "image": "terrian.png", },
                    ],
                },
            ],
        }
    },
}

solves = {
    "standard": {
        "cyclotron": {
            "map": {
                (0, 0): "Xa",
                (1, 0): "Xb",
                (0, 1): "CB",
                (1, 1): "Xc",
                (0, 2): "QR",
                (1, 2): "None"
            },
            "score": 2.6404
        },
        "infra": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "Xa",
                (0, 1): "Xc",
                (1, 1): "IK",
                (0, 2): "None",
                (1, 2): "QR"
            },
            "score": 2.5972
        },
        "phase": {
            "map": {
                (0, 0): "FD",
                (1, 0): "None",
                (0, 1): "PB",
                (1, 1): "Xc",
                (0, 2): "Xb",
                (1, 2): "Xa"
            },
            "score": 2.5808
        },
        "photon": {
            "map": {
                (0, 0): "Xc",
                (1, 0): "Xa",
                (0, 1): "Xb",
                (1, 1): "PC",
                (0, 2): "None",
                (1, 2): "NO"
            },
            "score": 2.6404
        },
        "positron": {
            "map": {
                (0, 0): "FS",
                (1, 0): "None",
                (0, 1): "PE",
                (1, 1): "Xa",
                (0, 2): "Xc",
                (1, 2): "Xb"
            },
            "score": 2.6404
        },
        "rocket": {
            "map": {
                (0, 0): "LR",
                (0, 1): "RL",
                (0, 2): "None"
            },
            "score": 1.14048
        },
        "shield": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "Xc",
                (0, 1): "Xa",
                (1, 1): "AA",
                (0, 2): "DS",
                (1, 2): "None"
            },
            "score": 1.099508
        },
        "hyper": {
            "map": {
                (0, 0): "ED",
                (1, 0): "Xc",
                (2, 0): "EW",
                (0, 1): "CD",
                (1, 1): "Xa",
                (2, 1): "Xb",
                (0, 2): "AD",
                (1, 2): "HD",
                (2, 2): "ID"
            },
            "score": 1.107644
        },
        "launch": {
            "map": {
                (0, 0): "EF",
                (1, 0): "LT",
                (0, 1): "Xa",
                (1, 1): "Xb",
                (0, 2): "Xc",
                (1, 2): "RC"
            },
            "score": 1.042243
        },
        "pulse": {
            "map": {
                (0, 0): "ID",
                (1, 0): "Xb",
                (2, 0): "FA",
                (3, 0): "None",
                (0, 1): "SL",
                (1, 1): "Xa",
                (2, 1): "Xc",
                (3, 1): "PE"
            },
            "score": 1.92674
        },
        "photonix": {
            "map": {
                (0, 0): "ID",
                (1, 0): "Xa",
                (2, 0): "Xb",
                (3, 0): "SL",
                (0, 1): "PE",
                (1, 1): "PC",
                (2, 1): "Xc",
                (3, 1): "FA"
            },
            "score": 2.260143
        },
        "trails": {
            "map": {
                (0, 0): "None",
                (1, 0): "RT",
                (2, 0): "CT",
                (3, 0): "TT",
                (0, 1): "SB",
                (1, 1): "AB",
                (2, 1): "PB",
                (3, 1): "ET",
                (0, 2): "None",
                (1, 2): "GT",
                (2, 2): "ST",
                (3, 2): "SP"
            },
            "score": 0.162
        }
    },
    "sentinel": {
        "cyclotron": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "Xa",
                (0, 1): "Xc",
                (1, 1): "CB",
                (0, 2): "None",
                (1, 2): "QR"
            },
            "score": 2.6404
        },
        "infra": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "Xa",
                (0, 1): "IK",
                (1, 1): "Xc",
                (0, 2): "QR",
                (1, 2): "None"
            },
            "score": 2.6404
        },
        "phase": {
            "map": {
                (0, 0): "Xa",
                (1, 0): "Xb",
                (0, 1): "Xc",
                (1, 1): "PB",
                (0, 2): "None",
                (1, 2): "FD"
            },
            "score": 2.5808
        },
        "positron": {
            "map": {
                (0, 0): "Xa",
                (1, 0): "Xb",
                (0, 1): "PE",
                (1, 1): "Xc",
                (0, 2): "FS",
                (1, 2): "None"
            },
            "score": 2.6404
        },
        "rocket": {
            "map": {
                (0, 0): "LR",
                (0, 1): "RL",
                (0, 2): "None"
            },
            "score": 1.14048
        },
        "photon": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "Xc",
                (0, 1): "Xa",
                (1, 1): "PC",
                (0, 2): "None",
                (1, 2): "NO"
            },
            "score": 2.6404
        },
        "shield": {
            "map": {
                (0, 0): "DS",
                (1, 0): "None",
                (0, 1): "Xa",
                (1, 1): "Xc",
                (0, 2): "AA",
                (1, 2): "Xb"
            },
            "score": 1.099508
        },
        "launch": {
            "map": {
                (0, 0): "RC",
                (1, 0): "Xc",
                (0, 1): "Xa",
                (1, 1): "Xb",
                (0, 2): "EF",
                (1, 2): "LT"
            },
            "score": 1.042243
        },
        "hyper": {
            "map": {
                (0, 0): "ED",
                (1, 0): "CD",
                (2, 0): "ID",
                (0, 1): "Xb",
                (1, 1): "Xa",
                (2, 1): "HD",
                (0, 2): "EW",
                (1, 2): "Xc",
                (2, 2): "AD"
            },
            "score": 1.1076556
        },
        "pulse": {
            "map": {
                (0, 0): "FA",
                (1, 0): "Xb",
                (2, 0): "ID",
                (3, 0): "None",
                (0, 1): "Xc",
                (1, 1): "Xa",
                (2, 1): "PE",
                (3, 1): "SL"
            },
            "score": 3.1744
        },
        "trails": {
            "map": {
                (0, 0): "None",
                (1, 0): "RT",
                (2, 0): "CT",
                (3, 0): "TT",
                (0, 1): "SB",
                (1, 1): "AB",
                (2, 1): "PB",
                (3, 1): "ET",
                (0, 2): "None",
                (1, 2): "GT",
                (2, 2): "ST",
                (3, 2): "SP"
            },
            "score": 0.162
        }
    },
    "living": {
        "grafted": {
            "map": {
                (0, 0): "Xa",
                (1, 0): "Xc",
                (0, 1): "Xb",
                (1, 1): "GE"
            },
            "score": 2.4787
        },
        "spewing": {
            "map": {
                (0, 0): "Xc",
                (1, 0): "Xb",
                (0, 1): "Xa",
                (1, 1): "SV"
            },
            "score": 2.5172
        },
        "scream": {
            "map": {
                (0, 0): "SS",
                (1, 0): "Xc",
                (0, 1): "Xb",
                (1, 1): "Xa"
            },
            "score": 0.980816
        },
        "assembly": {
            "map": {
                (0, 0): "NA",
                (1, 0): "None",
                (0, 1): "Xa",
                (1, 1): "Xb",
                (0, 2): "Xc",
                (1, 2): "CM"
            },
            "score": 1.018424
        },
        "singularity": {
            "map": {
                (0, 0): "Xc",
                (1, 0): "Xb",
                (0, 1): "AD",
                (1, 1): "Xa",
                (0, 2): "None",
                (1, 2): "SC"
            },
            "score": 1.088624
        },
        "pulsing": {
            "map": {
                (0, 0): "Xa",
                (1, 0): "Xc",
                (0, 1): "Xb",
                (1, 1): "PH"
            },
            "score": 1.656816
        },
        "trails": {
            "map": {
                (0, 0): "None",
                (1, 0): "RT",
                (2, 0): "CT",
                (3, 0): "TT",
                (0, 1): "SB",
                (1, 1): "AB",
                (2, 1): "PB",
                (3, 1): "ET",
                (0, 2): "None",
                (1, 2): "GT",
                (2, 2): "ST",
                (3, 2): "SP"
            },
            "score": 0.162
        }
    },
    "standard-mt": {
        "mining": {
            "map": {
                (0, 0): "AM",
                (1, 0): "Xb",
                (0, 1): "MB",
                (1, 1): "OD",
                (0, 2): "Xc",
                (1, 2): "Xa"
            },
            "score": 2.324348
        },
        "scanner": {
            "map": {
                (0, 0): "SC",
                (1, 0): "Xc",
                (2, 0): "WR",
                (3, 0): "None",
                (0, 1): "PC",
                (1, 1): "Xb",
                (2, 1): "Xa",
                (3, 1): "SH"
            },
            "score": 6.8525
        },
        "blaze-javelin": {
            "map": {
                (0, 0): "WO",
                (1, 0): "Xc",
                (0, 1): "Xb",
                (1, 1): "BJ",
                (0, 2): "Xa",
                (1, 2): "MA"
            },
            "score": 1.6088
        },
        "bolt-caster": {
            "map": {
                (0, 0): "RM",
                (1, 0): "Xc",
                (0, 1): "BC",
                (1, 1): "Xa",
                (0, 2): "BI",
                (1, 2): "Xb"
            },
            "score": 1.380922
        },
        "geology": {
            "map": {
                (0, 0): "GC",
                (1, 0): "Xc",
                (0, 1): "Xa",
                (1, 1): "Xb"
            },
            "score": 2.1692
        },
        "neutron": {
            "map": {
                (0, 0): "PF",
                (1, 0): "None",
                (0, 1): "Xa",
                (1, 1): "Xb",
                (0, 2): "Xc",
                (1, 2): "NC"
            },
            "score": 7.404
        },
        "plasma-launcher": {
            "map": {
                (0, 0): "Xc",
                (1, 0): "Xa",
                (0, 1): "PL",
                (1, 1): "Xb"
            },
            "score": 2.1692
        },
        "pulse-splitter": {
            "map": {
                (0, 0): "Xc",
                (1, 0): "Xa",
                (2, 0): "Xb",
                (3, 0): "None",
                (0, 1): "AC",
                (1, 1): "PS",
                (2, 1): "RM",
                (3, 1): "II"
            },
            "score": 2.273432
        },
        "scatter": {
            "map": {
                (0, 0): "SG",
                (1, 0): "None",
                (0, 1): "SB",
                (1, 1): "Xc",
                (0, 2): "Xa",
                (1, 2): "Xb"
            },
            "score": 2.249308
        }
    },
    "atlantid": {
        "mining": {
            "map": {
                (0, 0): "AM",
                (1, 0): "MB",
                (2, 0): "OD",
                (3, 0): "Xa",
                (0, 1): "Xb",
                (1, 1): "RL",
                (2, 1): "Xc",
                (3, 1): "None"
            },
            "score": 3.56434
        },
        "scanner": {
            "map": {
                (0, 0): "PC",
                (1, 0): "Xa",
                (2, 0): "Xb",
                (3, 0): "SH",
                (0, 1): "SC",
                (1, 1): "Xc",
                (2, 1): "WR",
                (3, 1): "None"
            },
            "score": 6.8525
        },
        "blaze-javelin": {
            "map": {
                (0, 0): "WO",
                (1, 0): "Xc",
                (0, 1): "Xb",
                (1, 1): "BJ",
                (0, 2): "MA",
                (1, 2): "Xa"
            },
            "score": 1.6088
        },
        "bolt-caster": {
            "map": {
                (0, 0): "RM",
                (1, 0): "Xb",
                (0, 1): "BC",
                (1, 1): "Xa",
                (0, 2): "BI",
                (1, 2): "Xc"
            },
            "score": 1.380922
        },
        "geology": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "GC",
                (0, 1): "Xa",
                (1, 1): "Xc"
            },
            "score": 2.1692
        },
        "neutron": {
            "map": {
                (0, 0): "NC",
                (1, 0): "Xc",
                (0, 1): "Xb",
                (1, 1): "Xa",
                (0, 2): "None",
                (1, 2): "PF"
            },
            "score": 7.404
        },
        "plasma-launcher": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "Xa",
                (0, 1): "PL",
                (1, 1): "Xc"
            },
            "score": 2.1692
        },
        "pulse-splitter": {
            "map": {
                (0, 0): "II",
                (1, 0): "Xc",
                (2, 0): "Xa",
                (3, 0): "Xb",
                (0, 1): "None",
                (1, 1): "RM",
                (2, 1): "PS",
                (3, 1): "AC"
            },
            "score": 2.273432
        },
        "scatter": {
            "map": {
                (0, 0): "Xc",
                (1, 0): "Xa",
                (0, 1): "Xb",
                (1, 1): "SB",
                (0, 2): "None",
                (1, 2): "SG"
            },
            "score": 2.249308
        }
    },
    "sentinel-mt": {
        "mining": {
            "map": {
                (0, 0): "AM",
                (1, 0): "Xb",
                (0, 1): "OD",
                (1, 1): "MB",
                (0, 2): "Xc",
                (1, 2): "Xa"
            },
            "score": 2.324348
        },
        "scanner": {
            "map": {
                (0, 0): "SH",
                (1, 0): "Xa",
                (2, 0): "Xb",
                (3, 0): "PC",
                (0, 1): "SC",
                (1, 1): "Xc",
                (2, 1): "WR",
                (3, 1): "None"
            },
            "score": 6.8525
        },
        "blaze-javelin": {
            "map": {
                (0, 0): "WO",
                (1, 0): "Xc",
                (0, 1): "Xb",
                (1, 1): "BJ",
                (0, 2): "Xa",
                (1, 2): "MA"
            },
            "score": 1.6088
        },
        "bolt-caster": {
            "map": {
                (0, 0): "BI",
                (1, 0): "Xb",
                (0, 1): "BC",
                (1, 1): "Xa",
                (0, 2): "RM",
                (1, 2): "Xc"
            },
            "score": 1.380922
        },
        "geology": {
            "map": {
                (0, 0): "GC",
                (1, 0): "Xa",
                (0, 1): "Xb",
                (1, 1): "Xc"
            },
            "score": 2.1692
        },
        "neutron": {
            "map": {
                (0, 0): "NC",
                (1, 0): "Xb",
                (0, 1): "Xa",
                (1, 1): "Xc",
                (0, 2): "PF",
                (1, 2): "None"
            },
            "score": 7.404
        },
        "plasma-launcher": {
            "map": {
                (0, 0): "Xb",
                (1, 0): "Xa",
                (0, 1): "Xc",
                (1, 1): "PL"
            },
            "score": 2.1692
        },
        "pulse-splitter": {
            "map": {
                (0, 0): "II",
                (1, 0): "Xb",
                (2, 0): "Xa",
                (3, 0): "Xc",
                (0, 1): "None",
                (1, 1): "AC",
                (2, 1): "PS",
                (3, 1): "RM"
            },
            "score": 2.273432
        },
        "scatter": {
            "map": {
                (0, 0): "Xc",
                (1, 0): "Xa",
                (0, 1): "SB",
                (1, 1): "Xb",
                (0, 2): "SG",
                (1, 2): "None"
            },
            "score": 2.249308
        }
    }
}
# fmt:on
