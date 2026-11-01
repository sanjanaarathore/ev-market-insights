/**
 * ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS
 * Interactive JavaScript Engine: Story Navigation, Embed Configurator, and Spec Comparator
 */

document.addEventListener('DOMContentLoaded', function () {
    // 1. Story Scene Tab Navigation
    const storyTabs = document.querySelectorAll('.story-tab');
    const sceneBadge = document.getElementById('sceneBadge');
    const sceneTitle = document.getElementById('sceneTitle');
    const sceneBody = document.getElementById('sceneBody');
    const sceneStats = document.getElementById('sceneStats');

    const scenesData = {
        '1': {
            badge: 'Scene 1 of 7',
            title: 'Global EV Market Overview',
            body: 'The global electric vehicle landscape has reached mature commercial scale across 299,999 evaluated vehicle records, spanning 17,980 commercial models, 200 automotive manufacturers, and 10 manufacturing nations. With cumulative annual fleet sales exceeding 2.34 billion units and an average certified driving range of 324.5 km, electrification is penetrating every consumer, commercial, and micro-mobility segment.',
            stats: [
                { icon: 'fa-car', text: '299,999 Fleet Records' },
                { icon: 'fa-industry', text: '200 Global OEMs' },
                { icon: 'fa-bolt', text: '324.5 km Avg Range' },
                { icon: 'fa-chart-line', text: '2.34B Annual Sales' }
            ]
        },
        '2': {
            badge: 'Scene 2 of 7',
            title: 'EV Category Dynamics & Volume Foundation',
            body: 'Urban and micro-mobility solutions represent the volume foundation of the electric transition. Two-Wheeler Scooters lead global offerings with 29,478 models (9.83% of the fleet), followed closely by Sedans (25,851 models, 8.62%), Hatchbacks (25,713 models, 8.57%), and Compact SUVs (25,706 models, 8.57%). Conversely, heavy commercial vehicles (Electric Buses and Trucks) comprise 9.62% of the fleet but serve high-tonnage transit requirements with battery capacities up to 410 kWh.',
            stats: [
                { icon: 'fa-motorcycle', text: 'Scooters: 29.5k Models' },
                { icon: 'fa-car', text: 'Sedans: 25.8k Models' },
                { icon: 'fa-bus', text: 'Buses: 12.9k Models' },
                { icon: 'fa-truck', text: 'Trucks: 15.9k Models' }
            ]
        },
        '3': {
            badge: 'Scene 3 of 7',
            title: 'OEM Competitive Landscape & Portfolio Dispersion',
            body: 'Competition in the global electric vehicle ecosystem is remarkably distributed across 200 automotive OEMs, with no single manufacturer establishing a monopolistic stranglehold. The market leader by model diversity, VoltWorks, accounts for 1,627 models (0.54% share), followed by VelocityGroup (1,611 models), CircuitWorks (1,597 models), and AmpereGroup (1,589 models). By sales volume, AmpereWorks leads with 13.84 million units delivered.',
            stats: [
                { icon: 'fa-industry', text: 'VoltWorks: 1,627 Models' },
                { icon: 'fa-industry', text: 'VelocityGroup: 1,611 Models' },
                { icon: 'fa-trophy', text: 'AmpereWorks: 13.8M Sales' },
                { icon: 'fa-scale-balanced', text: 'Zero Monopoly (<0.6% share)' }
            ]
        },
        '4': {
            badge: 'Scene 4 of 7',
            title: 'Battery Technology Matrix & Cell Durability',
            body: 'Cathode chemistry remains the decisive battleground for vehicle performance and manufacturing cost. NMC (Nickel Manganese Cobalt) and LFP (Lithium Iron Phosphate) together dominate nearly 66% of the global market (NMC: 101,508 models, 33.84%; LFP: 96,137 models, 32.05%). LFP delivers superior longevity (mean 2,501 cycles) and low 5-year degradation (10.12%), while Solid-State technology commands premium adoption with an industry-leading 2,998 rated cycle life.',
            stats: [
                { icon: 'fa-battery-full', text: 'NMC: 33.84% Share' },
                { icon: 'fa-battery-half', text: 'LFP: 32.05% (2,501 Cycles)' },
                { icon: 'fa-gem', text: 'Solid-State: 2,998 Cycles' },
                { icon: 'fa-atom', text: 'Sodium-Ion: 10.0% Entry' }
            ]
        },
        '5': {
            badge: 'Scene 5 of 7',
            title: 'Annual EV Sales Trajectory by Model Year',
            body: 'Analyzing sales across model release vintages (2018 to 2026) reveals consistent annual delivery volumes, maintaining a steady baseline between 255.2 million and 265.7 million units per vintage. Model year 2019 marks the historical peak with 265.7 million units delivered, while newer vintages (2024: 264.9M; 2025: 257.1M; 2026: 257.2M) demonstrate sustained commercial adoption as fleet renewal cycles continue.',
            stats: [
                { icon: 'fa-calendar', text: '2019 Peak: 265.7M Units' },
                { icon: 'fa-calendar-check', text: '2024 Vintage: 264.9M Units' },
                { icon: 'fa-chart-line', text: 'Steady ~258M Units/Year' },
                { icon: 'fa-repeat', text: 'Active Fleet Renewal' }
            ]
        },
        '6': {
            badge: 'Scene 6 of 7',
            title: 'Manufacturing Geography & Sovereign Assembly Hubs',
            body: 'Vehicle assembly is distributed across 10 sovereign automotive manufacturing hubs. India leads global assembly with 30,285 models (10.10%), followed by South Korea (30,155 models, 10.05%), China (30,142 models, 10.05%), Vietnam (30,030 models, 10.01%), and the United States (30,029 models, 10.01%). European manufacturing hubs (France, Germany, UK, Sweden) collectively contribute 29.87% of global vehicle models.',
            stats: [
                { icon: 'fa-earth-asia', text: 'Asia Clusters: 50.13% Share' },
                { icon: 'fa-flag', text: 'India: 30.3k Models' },
                { icon: 'fa-earth-europe', text: 'Europe Hubs: 29.87% Share' },
                { icon: 'fa-flag-usa', text: 'USA: 30.0k Models' }
            ]
        },
        '7': {
            badge: 'Scene 7 of 7',
            title: 'Strategic Takeaways, Pricing & Decarbonization ROI',
            body: 'Key Strategic Findings from the Global Fleet Analysis: 1) Commercial Electrification is the Highest-Impact Climate Lever: Electric Buses and Trucks abate ~9.0 metric tons of CO2 annually per vehicle—nearly 3x the impact of standard passenger cars (3.04 tons/yr). 2) Battery Sizing Dictates Capital Cost: Installed battery capacity exhibits a dominant r = +0.8373 correlation with vehicle price. 3) Customer Satisfaction is Universally High: Across all 15 segments, average owner satisfaction remains clustered at 4.09★ out of 5.0.',
            stats: [
                { icon: 'fa-leaf', text: 'Buses: 9.04 t/yr CO2 Saved' },
                { icon: 'fa-dollar-sign', text: 'r = +0.8373 Battery Price' },
                { icon: 'fa-star', text: '4.09★ Universal Rating' },
                { icon: 'fa-circle-check', text: 'Phase 3 Web Integrated' }
            ]
        }
    };

    if (storyTabs.length > 0) {
        storyTabs.forEach(tab => {
            tab.addEventListener('click', function () {
                storyTabs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                const sceneId = this.getAttribute('data-scene');
                const data = scenesData[sceneId];
                if (data) {
                    sceneBadge.textContent = data.badge;
                    sceneTitle.textContent = data.title;
                    sceneBody.innerHTML = `<p>${data.body}</p>`;
                    sceneStats.innerHTML = data.stats.map(s => 
                        `<div class="stat-pill"><i class="fa-solid ${s.icon}"></i> ${s.text}</div>`
                    ).join('');
                }
            });
        });
    }

    // 2. Embed URL Configuration Modal
    const btnConfigure = document.getElementById('btn-configure-tableau');
    const configModal = document.getElementById('configModal');
    const modalClose = document.getElementById('modalClose');
    const btnCancelModal = document.getElementById('btnCancelModal');
    const btnSaveTableauUrl = document.getElementById('btnSaveTableauUrl');
    const inputDashboardUrl = document.getElementById('inputDashboardUrl');
    const tableauViz = document.getElementById('tableauViz');

    if (btnConfigure && configModal) {
        btnConfigure.addEventListener('click', () => configModal.classList.add('active'));
        if (modalClose) modalClose.addEventListener('click', () => configModal.classList.remove('active'));
        if (btnCancelModal) btnCancelModal.addEventListener('click', () => configModal.classList.remove('active'));
        
        if (btnSaveTableauUrl && inputDashboardUrl) {
            btnSaveTableauUrl.addEventListener('click', () => {
                const newUrl = inputDashboardUrl.value.trim();
                if (newUrl) {
                    if (tableauViz) {
                        tableauViz.setAttribute('src', newUrl);
                    }
                    const banner = document.getElementById('url-banner');
                    if (banner) {
                        banner.innerHTML = `<div class="banner-icon"><i class="fa-solid fa-circle-check"></i></div>
                        <div class="banner-text"><strong>Tableau Public Connected:</strong> Displaying live workbook from <code>${newUrl}</code></div>`;
                    }
                    configModal.classList.remove('active');
                }
            });
        }
    }

    // 3. Dedicated Tableau Page View Switcher (Dashboard vs Story)
    const btnShowDashboard = document.getElementById('btnShowDashboard');
    const btnShowStory = document.getElementById('btnShowStory');
    const dashboardEmbedBox = document.getElementById('dashboardEmbedBox');
    const storyEmbedBox = document.getElementById('storyEmbedBox');

    if (btnShowDashboard && btnShowStory && dashboardEmbedBox && storyEmbedBox) {
        btnShowDashboard.addEventListener('click', function () {
            btnShowDashboard.classList.add('active');
            btnShowStory.classList.remove('active');
            dashboardEmbedBox.classList.remove('d-none');
            storyEmbedBox.classList.add('d-none');
        });

        btnShowStory.addEventListener('click', function () {
            btnShowStory.classList.add('active');
            btnShowDashboard.classList.remove('active');
            storyEmbedBox.classList.remove('d-none');
            dashboardEmbedBox.classList.add('d-none');
        });
    }

    // 4. Interactive Spec Comparator
    const btnRunCompare = document.getElementById('btnRunCompare');
    const selectCat1 = document.getElementById('selectCat1');
    const selectCat2 = document.getElementById('selectCat2');

    if (btnRunCompare && selectCat1 && selectCat2) {
        btnRunCompare.addEventListener('click', function () {
            const cat1 = selectCat1.value;
            const cat2 = selectCat2.value;

            btnRunCompare.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Comparing...';

            fetch(`/api/spec-compare?cat1=${encodeURIComponent(cat1)}&cat2=${encodeURIComponent(cat2)}`)
                .then(res => res.json())
                .then(data => {
                    btnRunCompare.innerHTML = '<i class="fa-solid fa-play"></i> Compare Specifications';
                    if (data.segment1 && data.segment2) {
                        // Update Segment 1
                        const s1 = data.segment1;
                        document.getElementById('nameSeg1').textContent = s1.category;
                        document.getElementById('countSeg1').textContent = `${s1.models_count.toLocaleString()} Models Evaluated`;
                        document.getElementById('rangeSeg1').textContent = `${s1.avg_range} km`;
                        document.getElementById('batSeg1').textContent = `${s1.avg_battery} kWh`;
                        document.getElementById('priceSeg1').textContent = `$${s1.avg_price.toLocaleString()}`;
                        document.getElementById('effSeg1').textContent = `${s1.avg_efficiency} Wh/km`;
                        document.getElementById('accSeg1').textContent = `${s1.avg_acceleration} s`;
                        document.getElementById('ratSeg1').textContent = `${s1.avg_rating} ★`;
                        document.getElementById('co2Seg1').textContent = `${s1.avg_co2_saved} tons/yr`;

                        // Update Segment 2
                        const s2 = data.segment2;
                        document.getElementById('nameSeg2').textContent = s2.category;
                        document.getElementById('countSeg2').textContent = `${s2.models_count.toLocaleString()} Models Evaluated`;
                        document.getElementById('rangeSeg2').textContent = `${s2.avg_range} km`;
                        document.getElementById('batSeg2').textContent = `${s2.avg_battery} kWh`;
                        document.getElementById('priceSeg2').textContent = `$${s2.avg_price.toLocaleString()}`;
                        document.getElementById('effSeg2').textContent = `${s2.avg_efficiency} Wh/km`;
                        document.getElementById('accSeg2').textContent = `${s2.avg_acceleration} s`;
                        document.getElementById('ratSeg2').textContent = `${s2.avg_rating} ★`;
                        document.getElementById('co2Seg2').textContent = `${s2.avg_co2_saved} tons/yr`;
                    }
                })
                .catch(err => {
                    console.error('Error fetching spec comparison:', err);
                    btnRunCompare.innerHTML = '<i class="fa-solid fa-play"></i> Compare Specifications';
                });
        });
    }
});

