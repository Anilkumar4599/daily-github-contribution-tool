\# QC Defect Classification — ATM Surveillance Devices



\## Purpose



This document provides a sample classification of common defects

that may be identified during QC inspection of ATM surveillance

equipment.



\## Assumptions



\- This is a sample dataset created for learning and demonstration.

\- The defect records are hypothetical and are not actual company data.

\- Severity is classified as Critical, Major, or Minor.

\- Each defect represents one sample observation.

\- Possible causes are initial hypotheses and require RCA/technical validation.



\## Defect Classification Table



| Defect ID | Device | Defect Description | Category | Severity | Possible Cause | QC Action | Status |

|---|---|---|---|---|---|---|---|

| DEF-001 | Main Unit | Unit does not power ON | Power | Critical | Power supply / PCB issue | Check input voltage and replace faulty unit | Open |

| DEF-002 | Lobby Camera | No video output | Video | Critical | Camera / cable / connector issue | Check camera, cable and connector | Open |

| DEF-003 | Backroom Camera | Poor image quality | Video | Major | Lens / focus / lighting issue | Check lens, focus and lighting | In Review |

| DEF-004 | Outdoor Camera | Camera restarts intermittently | Stability | Major | Power instability / firmware issue | Check power and firmware | Open |

| DEF-005 | Router | Network connection drops | Network | Major | SIM / signal / router issue | Check SIM, signal and router configuration | Open |

| DEF-006 | Sensor Bag | Sensor not detected | Sensor | Major | Sensor connection / sensor failure | Check wiring and replace sensor if required | Open |

| DEF-007 | PCMU | Device communication failure | Communication | Critical | Communication interface / hardware issue | Perform communication test | Open |

| DEF-008 | DCUPS | Backup power not available | Power | Critical | Battery / charging circuit issue | Test battery and charging circuit | Open |

| DEF-009 | Lobby Unit | Button/display issue | Functional | Minor | Component / connection issue | Functional inspection and repair | In Review |

| DEF-010 | Main Unit | Label/serial number mismatch | Documentation | Minor | Incorrect labeling | Verify against system records | Closed |



\## Defect Summary



| Category | Number of Defects |

|---|---:|

| Power | 2 |

| Video | 2 |

| Stability | 1 |

| Network | 1 |

| Sensor | 1 |

| Communication | 1 |

| Functional | 1 |

| Documentation | 1 |



\## Severity Summary



| Severity | Number of Defects |

|---|---:|

| Critical | 4 |

| Major | 4 |

| Minor | 2 |



\## QA Management Observations



1\. Power-related issues should receive high priority because they can prevent equipment from operating.

2\. Video-related defects can directly affect surveillance footage availability.

3\. Network and router issues should be monitored for recurring failures.

4\. Repeated defects should be investigated through Root Cause Analysis (RCA).

5\. Critical defects should not be released to shipment without resolution or approved deviation.

6\. Defect trends should be reviewed weekly to identify recurring device or supplier problems.



\## Next Improvement



This sample table can later be converted into:



\- Excel QC tracker

\- Power BI QC dashboard

\- Python defect analysis

\- Automated management report

