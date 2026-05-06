import streamlit as st

    # --------------------------------------------------------
    # MODEL PREDICTIONS
    # --------------------------------------------------------

    st.header("🤖 Model Predictions")

    rf_pred = rf.predict(X)[0]

    svm_pred = svm.predict(X)[0]

    cnn_pred = np.argmax(
        cnn.predict(X),
        axis=1
    )[0]

    preds = [rf_pred, svm_pred, cnn_pred]

    ensemble = max(
        set(preds),
        key=preds.count
    )

    label_map = {

        0: "0 ft-lbs (Loose)",
        1: "25 ft-lbs",
        2: "50 ft-lbs (Tight)"
    }

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Random Forest",
        label_map[rf_pred]
    )

    col2.metric(
        "SVM",
        label_map[svm_pred]
    )

    col3.metric(
        "CNN",
        label_map[cnn_pred]
    )

    col4.metric(
        "Ensemble",
        label_map[ensemble]
    )

    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------

    st.header("✅ Final Prediction")

    st.success(
        f"Predicted Torque Condition: {label_map[ensemble]}"
    )

    # --------------------------------------------------------
    # FEATURE TABLE
    # --------------------------------------------------------

    st.header("📊 Extracted Features")

    feature_df = pd.DataFrame(
        features.reshape(1,-1)
    )

    st.dataframe(feature_df)

    # --------------------------------------------------------
    # CLEANUP
    # --------------------------------------------------------

    os.remove(temp_path)

else:

    st.info("Upload an audio file to begin analysis.")
