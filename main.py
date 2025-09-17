# -*- coding: utf-8 -*-
"""
Main script to demonstrate the functionalities of the RooR package.
"""

from src.RooR import behavioral_analysis, attack_simulation, report_generation
import pandas as pd
import os

def main():
    """
    Main function to run the demonstration.
    """
    print("--- Starting RooR Demonstration ---")

    # Create a directory for reports if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # 1. Simulate an attack
    print("\n--- Simulating Post-Quantum Attack ---")
    target = "Quantum-Resistant AI Model"
    attack_result = attack_simulation.simulate_lattice_based_attack(target)
    report_generation.generate_json_report(attack_result, "reports/attack_report.json")

    # 2. Analyze logs for anomalies
    print("\n--- Analyzing Logs for Anomalies ---")
    # Create a dummy log file for demonstration
    log_data = {
        'timestamp': pd.to_datetime(['2023-10-27 10:00:00', '2023-10-27 10:05:00', '2023-10-27 10:10:00', '2023-10-27 10:15:00']),
        'event_type': ['login', 'logout', 'login', 'failed_login']
    }
    log_df = pd.DataFrame(log_data)
    log_df.to_csv('dummy_logs.csv', index=False)
    
    anomalies = behavioral_analysis.analyze_logs('dummy_logs.csv')
    if not anomalies.empty:
        print("Anomalies detected:")
        print(anomalies)
        report_generation.generate_csv_report(anomalies, "reports/anomalies_report.csv")
    else:
        print("No anomalies detected.")

    # 3. Evaluate model resilience
    print("\n--- Evaluating Model Resilience ---")
    predictions = [1, 0, 1, 1, 0]
    ground_truth = [1, 0, 1, 0, 1]
    resilience = behavioral_analysis.evaluate_post_quantum_resilience(predictions, ground_truth)
    print(f"Model Resilience Metrics: {resilience}")
    report_generation.generate_json_report(resilience, "reports/resilience_report.json")

    print("\n--- RooR Demonstration Finished ---")
    print("Reports are saved in the 'reports' directory.")

if __name__ == "__main__":
    main()
