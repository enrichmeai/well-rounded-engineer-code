package com.enrichmeai.wre.javatour;

import java.util.Map;
import java.util.Optional;

/**
 * Java 8: {@link Optional}.
 *
 * <p>Optional makes "there may be no answer" part of the method's signature, so the caller has to
 * decide what to do about it instead of meeting a {@code NullPointerException} later.
 */
public final class OptionalValues {

    private final Map<String, String> emailsByUser;

    public OptionalValues(Map<String, String> emailsByUser) {
        this.emailsByUser = Map.copyOf(emailsByUser);
    }

    /** The user's email, if we know it. */
    public Optional<String> emailOf(String user) {
        return Optional.ofNullable(emailsByUser.get(user));
    }

    /** The domain of the user's email, or "unknown". Shows map, filter and orElse chained together. */
    public String domainOf(String user) {
        return emailOf(user)
                .filter(email -> email.contains("@"))
                .map(email -> email.substring(email.indexOf('@') + 1))
                .orElse("unknown");
    }
}
