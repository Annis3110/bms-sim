def run_simulation(pack, bms, kalman_estimators, current_profile, dt=1):
    log = []
    for t in range(len(current_profile)):
        currents = current_profile[t]
        pack.update(currents, dt)
        faults = bms.monitor(t)

        row = [t]
        for i, cell in enumerate(pack.cells):
            soc_est = kalman_estimators[i].update(currents[i], dt, cell.voltage)
            row += [cell.soc, soc_est, cell.voltage, cell.temp_c]
        log.append(row)
    return log