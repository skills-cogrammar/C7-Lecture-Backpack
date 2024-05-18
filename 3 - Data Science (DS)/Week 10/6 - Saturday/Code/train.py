import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train):
    # Create a Random Forest Classifier
    # rf_classifier = RandomForestClassifier(random_state=42)
    
    # # Perform hyperparameter tuning using GridSearchCV
    # param_grid = {
    #     'n_estimators': [100, 200, 300],
    #     'max_depth': [None, 10, 20],
    #     'min_samples_split': [2, 5, 10]
    # }
    # grid_search = GridSearchCV(rf_classifier, param_grid, cv=5)
    # grid_search.fit(X_train, y_train)
    
    # # Train the classifier with the best parameters
    # best_rf_classifier = grid_search.best_estimator_
    # best_rf_classifier.fit(X_train, y_train)
    
    rf_classifier = RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, random_state=42)
    
    # Train the classifier
    rf_classifier.fit(X_train, y_train)

    # Save the trained model to a file
    with open('trained_model.pkl', 'wb') as file:
        pickle.dump(rf_classifier, file)
    
    return rf_classifier