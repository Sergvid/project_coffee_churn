
def add_new_features(df):
    df = df.copy()

    df["is_subscribed"] = (df["subscription_status"] != "none").astype(float)
    df["spend_ratio"]   = df["total_spent_last_week"] / (
        df["total_spent_last_month"] + 1)
    df["rating_change"] = df["review_rating_last_1"] - df["review_rating_last_10"]
    df["freq_ratio"]    = df["order_frequency_week"] / (
        df["order_frequency_month"] + 1)
    df["sqrt_total_spent_month"] = np.sqrt(df["total_spent_last_month"].clip(0))
    df["sqrt_days_since_promo"]  = np.sqrt(df["days_since_last_promo"].clip(0))
    df["sqrt_app_opens"]         = np.sqrt(df["app_opens_per_week"].clip(0))
    df["days_since_order_sq"]    = df["days_since_last_order"] ** 2
    df["avg_order_value_sq"]     = df["avg_order_value"] ** 2
    df["discount_usage_sq"]      = df["discount_usage_rate"] ** 2

    return df
