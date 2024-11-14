# views.py
from django.contrib import messages, auth
from django.contrib.auth import login as auth_login, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from auditapp.forms import SignUpForm, FacilityAuditForm
from .forms import SignUpForm
from django.urls import reverse
from .models import FacilityAuditnew
from django.shortcuts import render, redirect
from .models import AuditResponsenew, AuditSummary
from django.shortcuts import render
import plotly.express as px
import pandas as pd
from .models import Indication


def dashboard(request):
    username = request.user.username  # Assuming user is logged in
    return render(request, 'login.html', {'username': username})

def base(request):
    username = request.user.username
    return render(request,'base.html',{'username': username})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('audit_selection')  # Change 'dashboard' to your desired redirect
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')

#signupview
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def audit_form_view(request):
    if request.method == 'POST':
        form = FacilityAuditForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('explanation_page')  # Redirect to a success page or another view
    else:
        form = FacilityAuditForm()
    return render(request, 'audit_form.html', {'form': form})

def explanation_view(request):
    username = request.user.username
    return render(request, 'explanation.html',{'username': username})

def facility_view(request):
    context = {
        'username': request.user.username,  # Passes the username to the template
    }
    return render(request, 'facility.html',context)

def ipc_audit_healthcare(request):
    return render(request, 'ipc_audit_healthcare.html')

def basefrm(request):
    return render(request, 'basefrm.html')

def ipc_audit_page(request, page_number):
    headings = {
        1: "Infection Prevention and Control Program",
        2: "Infection Prevention and Control Training",
        3: "Hand Hygiene",
        4: "Personal Protective Equipment (PPE)",
        5: "Respiratory Hygiene / Cough Etiquette",
        6: "Occupational Health",
        7: "IPC in Dental Setting",
        8: "IPC in Laboratory",
        9: "Medical Devices Reprocessing",
        10: "Waste management",
        11: "Laundry Services",
        12: "Environmental Cleaning",
    }


    elements = {
                1: [
                    {"ref_no": "1.1", "description": "At least one infection control focal point trained in IPC is available to manage the facility infection control program"},
                    {"ref_no": "1.2", "description": "The Infection control focal point is up to date with the current national guidelines and implemented in the facility"},
                    {"ref_no": "1.3", "description": "Updated GCC infection prevention and control manual is available and accessible for all HCWs"},
                    {"ref_no": "1.4", "description": "Facility has a system for early detection and management of potentially infectious persons at initial points of patient encounter (e.g. respiratory infectious patients)"},
                    {"ref_no": "1.5", "description": "IPC annual action plan is written according to risk assessment and implemented"},
                    {"ref_no": "1.6", "description": "There is documented IPC meeting with the facility in charge/ head to discuss IPC issues and risk assessment at least bio-annually"},
                    {"ref_no": "1.7", "description": "Report to IPC section in DGHS for any ; communicable diseases, infectious exposure, healthcare-associated infection (HAI), inoculation injury and audit result"},
                ],
                2: [
                    {"ref_no": "2.1", "description": "Education and Training on infection control done for newly recruited staff"},
                    {"ref_no": "2.2", "description": "Facility has a competency-based training program on infection prevention practices (HH, PPE, N95) for all HCWs"},
                    {"ref_no": "2.3", "description": "Facility has implemented a continuous education and training for HCWs on infection control and have coverage more than 80% of HCWs are trained"},
                    {"ref_no": "2.4", "description": "Provides education on infection prevention and control for patients, families, and visitors"},
                    {"ref_no": "2.5", "description": "Facility has a database for HCWs training in infection prevention and control"}
                ],
                3: [
                    {"ref_no": "3.1",
                     "description": "Hand hygiene facilities are available and accessible at the point of patient care (standardized sink, hand soap, hand rub and tissue)"},
                    {"ref_no": "3.2", "description": "Posters promoting hand hygiene are available and displayed"},
                    {"ref_no": "3.3",
                     "description": "Health care workers comply with hand hygiene recommendations, they can demonstrate appropriate hand hygiene techniques"},
                    {"ref_no": "3.4",
                     "description": "Hand washing sinks are dedicated only for hand washing procedure (not used to clean instruments)"},
                    {"ref_no": "3.5",
                     "description": "Conducting quarterly audits for hand hygiene compliance and provides feedback to HCWs, head of the facility and IPC in DGHS"}
                ],
                4: [
                    {"ref_no": "4.1",
                     "description": "Adequate amount of personal protective equipment are available and easily accessible with proper qualities (e.g., examination gloves, surgical masks, protective clothing, protective eyewear/face shields, N95, sterile gloves)"},
                    {"ref_no": "4.2",
                     "description": "HCWs can display appropriate technique of donning and doffing of personal protective equipment (correct sequence and appropriate technique including N95)"},
                    {"ref_no": "4.3",
                     "description": "HCWs use PPE according to risk assessment of the patients and changed between patients or when it is visibly soiled"},
                    {"ref_no": "4.4",
                     "description": "Staff are aware and comply with transmission-based precautions (start isolation of patients with communicable diseases and those who are colonized or infected with MDRO from other patients)"}
                ],
                5: [
                    {"ref_no": "5.1", "description": "Cough Etiquette posters are available and displayed"},
                    {"ref_no": "5.2",
                     "description": "Tissues and no-touch receptacles for disposal of tissues are provided near waiting areas"},
                    {"ref_no": "5.3",
                     "description": "Hand hygiene facilities are provided for patients to perform hand hygiene near waiting areas"},
                    {"ref_no": "5.4",
                     "description": "Face masks are offered to coughing patients and other infectious symptomatic persons from the entrance"}
                ],
                6: [
                    {"ref_no": "6.1",
                     "description": "The influenza vaccine is administered annually to targeted HCWs as per MOH recommendations"},
                    {"ref_no": "6.2",
                     "description": "Maintain the facility record of HCWs immunization e.g. (Flu, HBV, T-dap, MMR, Varicella)"},
                    {"ref_no": "6.3", "description": "Declaration form signed by HCWs who refuse immunization"},
                    {"ref_no": "6.4",
                     "description": "All HCWs have a baseline screening for hepatitis B, hepatitis C, HIV and tuberculosis (TB)"},
                    {"ref_no": "6.5",
                     "description": "HCWs aware and implement the national blood & body fluid exposure policy"},
                    {"ref_no": "6.6",
                     "description": "There is an implemented system for reporting, follow up, and management of sharp/needle stick injuries/blood and body fluid exposures"},
                    {"ref_no": "6.7",
                     "description": "Emergency eyewash safety station is available in Sterilization and Laboratory area and accessible within 30 meters/10 seconds of potential chemical exposure"}
                ],
                7: [
                    {"ref_no": "7.1",
                     "description": "Dental care personnel use one-handed recapping (scoop technique) for recapping needles"},
                    {"ref_no": "7.2",
                     "description": "Sharps containers are available at the point of use and positioned safely"},
                    {"ref_no": "7.3",
                     "description": "Protective disposable bibs and barriers are available; used for every procedure"},
                    {"ref_no": "7.4",
                     "description": "Clinical contact surfaces (e.g., light handles, bracket trays, switches on dental units and hoses to the air-water syringe) are either barrier protected (changed between patients) or cleaned and disinfected after each patient"},
                    {"ref_no": "7.5",
                     "description": "Implementation of zoning technique (clean and contaminated areas) in dental clinic"},
                    {"ref_no": "7.6",
                     "description": "Cleaning, disinfection, and sterilization processes are done in dedicated room"},
                    {"ref_no": "7.7", "description": "Reprocessing of dental instruments is carried by trained staff"},
                    {"ref_no": "7.8",
                     "description": "Sterilization quality indicators are available and used according to the recommendation"},
                    {"ref_no": "7.9", "description": "Sterile instruments are kept wrapped/packed and stored appropriately"},
                    {"ref_no": "7.10",
                     "description": "Regular maintenance of the dental units is done and all the filters in the unit are changed according to the manufacturer instruction"},
                    {"ref_no": "7.11",
                     "description": "Waterline used in dental unit should be treated as meeting standards for drinking water"},
                    {"ref_no": "7.12",
                     "description": "Sterile saline/sterile water is used as irrigate when performing surgical procedure"}
                ],
                8: [
            {"ref_no": "8.1", "description": "Access is restricted with a biohazard sign posted at the entrance"},
            {"ref_no": "8.2", "description": "Eating, drinking, handling contact lenses, and storing food are not permitted."},
            {"ref_no": "8.3",
             "description": "All surfaces, walls & floors are solid, non-porous, easy to clean and withstand frequent cleaning and disinfection"},
            {"ref_no": "8.4", "description": "PPE available and used by HCWs while dealing with suspect or infectious samples"},
            {"ref_no": "8.5", "description": "Spill kits (biological and chemical) are available"},
            ],
            9:[ {"ref_no": "9.1", "description": "Written guideline/SOP for cleaning, disinfection and sterilization of equipment is available and implemented"},
            {"ref_no": "9.2", "description": "Medical equipment (e.g., Humidifier, Stethoscope, Blood Pressure monitor, Otoscope) are cleaned/disinfected properly by assigned staff and as per manufacturer recommendations"},
            {"ref_no": "9.3", "description": "At least two staff are trained and able to explain all procedures of instruments reprocessing/sterilization"},
            {"ref_no": "9.4", "description": "Dedicated area for cleaning, disinfection, sterilization process (Physical separation between dirty and clean zone)"},
            {"ref_no": "9.5", "description": "Cleaning supplies are available (e.g., brushes with various shapes and sizes, detergents that are used as per policies & procedures, etc.)"},
            {"ref_no": "9.6", "description": "Disinfection done mechanically/manually as per manufacturer's recommendations and document the monitoring performance."},
            {"ref_no": "9.7", "description": "Instruments should be packed according to the standards with chemical indicator inside"},
            {"ref_no": "9.8", "description": "Operating instructions for sterilizers with records for preventive maintenance are available."},
            {"ref_no": "9.9", "description": "For each sterilization load, the following information is documented: Date, Load contents, cycle type, Operator's name and results of BI, if used."},
            {"ref_no": "9.10", "description": "Bowie-Dick test performed daily before the first processed in empty load"},
            {"ref_no": "9.11", "description": "Biological indicator is performed weekly and records of test results are kept"},
            {"ref_no": "9.12", "description": "Sterile instruments are kept wrapped/packed and stored appropriately"},
            {"ref_no": "9.13", "description": "Type of water used to fill in the water tank of sterilizer following the recommendation by the device manufacturer"},
            ],
            10:[ {"ref_no": "10.1", "description": "Maintain contract with authorized national company for medical waste disposal"},
            {"ref_no": "10.2", "description": "Waste segregation maintained by HCWs"},
            {"ref_no": "10.3", "description": "Availability of foot operated dustbins with color coded bags and function properly"},
            {"ref_no": "10.4", "description": "Waste storage area should be: adequate in space, away from traffic, secured, with biohazard sign, and made of easily cleanable material"},
            {"ref_no": "10.5", "description": "Medical waste bags/sharp containers are securely closed after being filled to 3/4 of its maximum capacity"},
            {"ref_no": "10.6", "description": "Sharp containers are wall mounted/held on a stand at points of production and easy to access"},
            {"ref_no": "10.7", "description": "Infectious medical waste is transported in closed carts with biohazard sign. Carts are cleaned after each use or at least daily"},
            ],
            11:[
                {"ref_no": "11.1", "description": "Ensure that linen are sent to approved external laundry"},
                {"ref_no": "11.2", "description": "Soiled linen are kept in soluble bag"},
                {"ref_no": "11.3",
                 "description": "Dirty/soiled linen bags are kept away from the floor by hanging them in a closed rack"},
                {"ref_no": "11.4", "description": "Clean linen are stored in clean cabinet away from dirty linen"},
            ],
             12:[
                 {"ref_no": "12.1",
                "description": "Written guideline/SOP for environmental cleaning & disinfection is available and implemented"},
                {"ref_no": "12.2",
                 "description": "Facility routinely audits (monitors and documents) adherence to environmental cleaning and disinfection procedures by using national audit of area environmental cleaning"},
                {"ref_no": "12.3",
                 "description": "All environmental surfaces (e.g., clinics, waiting room, etc.) are cleaned and documented, cleaning is done according to a schedule of cleaning activities log"},
                {"ref_no": "12.4",
                 "description": "Cleaning materials and disinfectants are available adequately and approved by IPC and used in accordance with manufacturer instructions (e.g., dilution, storage, shelf life, contact time, PPE)."},
                {"ref_no": "12.5",
                 "description": "Housekeepers are well trained on hand hygiene, proper use of PPE (PPE can include gloves, gowns, masks, and eye protection), methods of cleaning, and proper and safe mixing of chemicals."},
                {"ref_no": "12.6",
                 "description": "Reusable mops/cloths used to clean housekeeping surfaces are mechanically washed and dried before reuse"},
                {"ref_no": "12.7",
                 "description": "The facility implements integrated pest management by using an inspection checklist"}
            ],
            }
    page_elements = elements.get(page_number, [])
    if request.method == 'POST' :
        met_count = 0
        partially_met_count = 0
        not_met_count = 0
        comments = request.POST.get('comments', '')


        # Loop through each element and save the response
        for i, element in enumerate(page_elements):
            d_value = request.POST.get(f'd_{i + 1}')
            si_value = request.POST.get(f'si_{i + 1}')
            o_value = request.POST.get(f'o_{i + 1}')
            scoring_value = request.POST.get(f'scoring_{i + 1}')

            # Check if the response already exists for this element and page
            audit_response, created = AuditResponsenew.objects.update_or_create(
                page_number=page_number,
                ref_no=element['ref_no'],
                defaults={'response': scoring_value},
            )

            # Count responses
            if scoring_value == 'Met':
                met_count += 1
            elif scoring_value == 'Partially Met':
                partially_met_count += 1
            elif scoring_value == 'Not Met':
                not_met_count += 1

        # Update or create the AuditSummary for the given page_number
        AuditSummary.objects.update_or_create(
            heading=headings[page_number],
            defaults={
                'met_count': met_count,
                'partially_met_count': partially_met_count,
                'not_met_count': not_met_count,
                'comments': comments,
            }
        )

        # Redirect to next page or summary report
        if page_number < len(headings):  # Redirect to next page if not the last one
            return redirect('ipc_audit_page', page_number=page_number + 1)
        else:  # If it's the last page, redirect to the summary
            return redirect('audit_summary')

    context = {
        'elements': page_elements,
        'page_number': page_number,
        'heading': headings.get(page_number),
        'next_page_number': page_number + 1 if page_number < len(headings) else None,
        'total_pages': len(headings),
        'headings': headings,
        'username': request.user.username,  # Passes the username to the template
    }

    return render(request, 'ipc_audit_page.html', context)


def calculate_overall_score(met_count, partially_met_count, total_count):
    if total_count == 0:  # Avoid division by zero
        return 0
    score = (met_count + 0.5 * partially_met_count) / total_count * 100  # Example formula
    return round(score, 2)  # Return rounded to 2 decimal places


def audit_summary(request):
    facility_audit = FacilityAuditnew.objects.last()
    grand_met_total = 0
    grand_partially_met_total = 0
    grand_not_met_total = 0
    comments = []

    if request.method == 'POST':
        number_of_pages = 12  # Adjust based on your setup
        for i in range(number_of_pages):
            met_count = int(request.POST.get(f'met_count_{i}', 0))
            partially_met_count = int(request.POST.get(f'partially_met_count_{i}', 0))
            not_met_count = int(request.POST.get(f'not_met_count_{i}', 0))
            comment = request.POST.get(f'comment_{i}', '')  # Fetch comment from the form
            comments.append(comment)
            summary = AuditSummary(
                met_count=met_count,
                partially_met_count=partially_met_count,
                not_met_count=not_met_count,
                comments=comment
            )
            summary.save()

            grand_met_total += met_count
            grand_partially_met_total += partially_met_count
            grand_not_met_total += not_met_count

    # If not a POST request, calculate the totals from existing AuditSummary entries
    else:
        summaries = AuditSummary.objects.all()

        # Calculate the compliance percentage for each summary and round it
        for summary in summaries:
            total = summary.met_count + summary.partially_met_count + summary.not_met_count
            compliance_percentage = (summary.met_count / total * 100) if total else 0
            summary.compliance_percentage = round(compliance_percentage)  # Round to the nearest whole number
            comments.append(summary.comments)

        grand_met_total = sum(summary.met_count for summary in summaries)
        grand_partially_met_total = sum(summary.partially_met_count for summary in summaries)
        grand_not_met_total = sum(summary.not_met_count for summary in summaries)
    grand_total = grand_met_total + grand_partially_met_total + grand_not_met_total
    grand_overall_score = calculate_overall_score(grand_met_total, grand_partially_met_total, grand_total)
    context = {
        'facility_audit': facility_audit,
        'facility_name': facility_audit.facility_name if facility_audit else 'N/A',
        'audit_date': facility_audit.audit_date if facility_audit else 'N/A',
        'summaries': summaries,
        'grand_met_total': grand_met_total,
        'grand_partially_met_total': grand_partially_met_total,
        'grand_not_met_total': grand_not_met_total,
        'grand_overall_score': grand_overall_score,
        'username': request.user.username,
        'comments': comments,
        'head_of_institution':facility_audit.head_of_institution,  # Add Head of Institution
        'lead_auditor': facility_audit.lead_auditor, # Add Lead Auditor
    }
    # Add category data for chart
    context['categories'] = [summary.heading for summary in summaries]
    context['met_counts'] = [summary.met_count for summary in summaries]
    context['partially_met_counts'] = [summary.partially_met_count for summary in summaries]
    context['not_met_counts'] = [summary.not_met_count for summary in summaries]
    return render(request, 'audit_summary.html', context)



def audit_selection(request):
    context = {
        'username': request.user.username,  # Passes the username to the template
    }
    return render(request, 'audit_selection.html', context)

#Endoscopy_Audit
def endoscopy_audit(request):
    return render(request, 'baseendos.html')


def facility_endoscopy(request):
    number_options = list(range(1, 11))  # Create a list of numbers from 1 to 10
    return render(request, 'facilityendos.html', {'number_options': number_options})

def explanation2_view(request):
    context = {
        'username': request.user.username,
    }
    return render(request, 'explanation2.html', context)

def handhygienenew(request):
    context = {
        'username': request.user.username,  # Passes the username to the template
    }
    return render(request, 'handhygienenew.html',context)

def general_instruction(request):
    context = {
        'username': request.user.username,  # Passes the username to the template
    }
    return render(request, 'general_instruction.html',context)

def profcat(request):
    return render(request, 'profcat.html')

def opportunities(request):
    return render(request, 'opportunities.html')

def formselection(request):
    return render(request, 'formselection.html')

def new_opportunity(request):
    return render(request, 'new_opportunity.html')

def hhactionform(request):
    context = {
        'username': request.user.username,  # Passes the username to the template
    }
    return render(request, 'hhactionform.html',context)


def compliance_chart(request):
    indications = Indication.objects.all()

    # Calculate totals for each session
    total_act_hr = sum(ind.act_hr for ind in indications)
    total_opp_hr = sum(ind.opp_hr for ind in indications)
    total_act_hw = sum(ind.act_hw for ind in indications)
    total_opp_hw = sum(ind.opp_hw for ind in indications)

    # Compliance calculation formula
    hr_compliance = (total_act_hr / total_opp_hr * 100) if total_opp_hr else 0
    hw_compliance = (total_act_hw / total_opp_hw * 100) if total_opp_hw else 0
    context = {
        'indications': indications,
        'total_act_hr': total_act_hr,
        'total_opp_hr': total_opp_hr,
        'total_act_hw': total_act_hw,
        'total_opp_hw': total_opp_hw,
        'hr_compliance': hr_compliance,
        'hw_compliance': hw_compliance,
    }
    return render(request, 'compliance_chart.html', context)