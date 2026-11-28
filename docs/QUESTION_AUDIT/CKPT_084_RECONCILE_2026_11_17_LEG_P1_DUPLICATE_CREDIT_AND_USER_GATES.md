# CKPT-084 | Reconciliere corectivă a fișelor P1 LEG din 17 noiembrie 2026

## Fapt verificat pe GitHub

- **CKPT-082 din 16.11.2026 (LEG010/016/023/035/036/037/047/049)** raporta deja **207/568 unități și 262/822 ID-uri** documentate contextual. Acest checkpoint este baza reală înainte de CKPT-080–083 *din 17.11.2026*. Există două seturi diferite cu prefix CKPT080/081/082, din zile diferite: numele de checkpoint reutilizate NU identifică unic lotul.
- Cele patru fișiere noi din 17.11.2026 au fiecare câte 5 unități și ID-uri P1 analizate, în total **20 carduri**, dar **9 dintre ele fuseseră creditate deja** în CKPT-081/082 din 16.11.2026. Cumulul incremental raportat în mesajele și fișierele noastre 17.11 (192,197,202,207) și afirmația «20 noi» au fost GREȘITE.
- Dublurile exacte sunt: **G1-LEG-001, 038** în CKPT080_2026_11_17 (ambele în CKPT081_2026_11_16); **LEG-006** în CKPT081_2026_11_17 (deja CKPT081_2026_11_16); **LEG-010, 013, 014** în CKPT082_2026_11_17 (deja CKPT082_2026_11_16 pentru LEG010, CKPT081_2026_11_16 pentru LEG013/014); **LEG-008, 016, 018** în CKPT083_2026_11_17 (deja CKPT081_2026_11_16 pentru LEG008/018 și CKPT082_2026_11_16 pentru LEG016).
- Cele **11 unități și 11 ID-uri noi**, verificate după identitatea canonică din MASTER, sunt: **LEG-021/022/040** (CKPT080_2026_11_17); **LEG-002/003/004/005** (CKPT081_2026_11_17); **LEG-011/012** (CKPT082_2026_11_17); **LEG-007/009** (CKPT083_2026_11_17).
- **Totalul corectat: 218/568 unități și 273/822 ID-uri de grad** cu fișe contextuale documentate. Creștere reală de la ultimul cumul anterior 207/262: **+11/+11**, nu +20/+20. **0/822** aprobate pentru învățare.
- Duplicatele din 17.11 pot aduce argumente și surse suplimentare, dar au `COVERAGE_DELTA=0`; istoria rămâne intactă pentru transparență și comparație. Acesta este un **fix contabil**, nu un verdict tehnic/juridic și nu include revalidare independentă de surse sau ediții.

## Ce necesită utilizatorul versus QA independent

- **Deja clarificat explicit de utilizator, nu mai întrebați:** NOR012 C, NOR030 B sugerat dar retras după dovada pozitivă pentru A din PE155, NOR031 B, NOR042 A, LEG028 C, ELE128 interpretarea istorică A, ELE222 intenția C, ELE053 raportarea utilizatorului despre baremul ANRE C (neconfirmat din cheia oficială), ELE126 A, NOR090 B ca intenție contextuală. Separarea între interpretarea userului și dovada oficială este obligatorie.
- **Candidat viitor de interpretare numai după citarea sursei complete:** G1-NOR-053 «branșament» vs «racord» (A vs C, definiție exactă și normă/ediție), LEG011 «ziar local» vs «publicație de largă circulație» (toate variantele afectate); alte conflicte semantice numai după sursa pozitivă + contraexemple.
- **Nu cereți acum de la utilizator:** aprobarea baremelor prin ghicire, stabilirea ediției legale 2026, găsirea manualelor ori QA independent; aceste lucruri sunt responsabilitatea auditului. **Aprobarea explicită pentru orice modificare canonică** se cere numai după pachetul final cu dovezi, corecții propuse, impact și QA.
- Fără schimbări de enunț, A/B/C, chei, master, HTML/APK, main, merge sau release; PR #7 păstrat Draft.
