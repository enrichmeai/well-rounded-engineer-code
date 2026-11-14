// A small load test for the tip-splitter API, written for Grafana k6.
// Run it against a running app:  k6 run -e BASE_URL=http://127.0.0.1:8000 k6/load-test.js
//
// It ramps up to 10 virtual users, holds, and ramps down (about 30 seconds in all), and fails if the
// 95th percentile response time is 500 ms or more, or if more than 1% of the checks fail.
import http from "k6/http";
import { check, sleep } from "k6";
import { Rate } from "k6/metrics";

const BASE_URL = __ENV.BASE_URL || "http://127.0.0.1:8000";
const failureRate = new Rate("check_failure_rate");

export const options = {
  stages: [
    { duration: "10s", target: 10 },
    { duration: "10s", target: 10 },
    { duration: "10s", target: 0 },
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"],
    check_failure_rate: ["rate<0.01"],
  },
};

export default function () {
  const response = http.get(`${BASE_URL}/api/split?total=60&people=3&tip=10`);
  const ok = check(response, {
    "status is 200": (r) => r.status === 200,
    "each person pays 22.00": (r) => r.json().per_person === "22.00",
  });
  failureRate.add(!ok);
  sleep(1);
}
