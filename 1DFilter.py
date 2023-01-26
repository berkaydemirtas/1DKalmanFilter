class OneDimensionKalmanFilter:
    def __init__(self,measurement_uncertanity,initial_guess,measurements,estimate_uncertanity):
        self.measurement_uncertanity = measurement_uncertanity
        self.initial_guess = initial_guess
        self.measurements = measurements
        self.estimate_uncertanity = estimate_uncertanity
        self.kalman_gain = 0
        self.current_state = initial_guess
        
    def calculate_kalman_gain(self):
        self.kalman_gain = self.estimate_uncertanity / (self.estimate_uncertanity + self.measurement_uncertanity)
        return self.kalman_gain
        
    def estimate_current_state(self, measurement):
        self.current_state = self.current_state + self.kalman_gain*(measurement - self.current_state)
        return self.current_state
        
    def update_estimate_uncertanity(self):
        self.estimate_uncertanity = (1-self.kalman_gain)*self.estimate_uncertanity
        return self.estimate_uncertanity
        
    def iterate(self):
        for measurement in self.measurements:
            print(self.current_state, self.kalman_gain, measurement)
            self.calculate_kalman_gain()
            self.estimate_current_state(measurement)
            self.update_estimate_uncertanity()
    
kalman_filter = OneDimensionKalmanFilter(25,60,[48.54,47.11,55.01],225)
kalman_filter.iterate()
            
            

        