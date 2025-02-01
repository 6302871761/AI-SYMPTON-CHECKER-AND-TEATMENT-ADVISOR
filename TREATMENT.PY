import React, { useState } from 'react';
import { Card, CardContent, Button, Textarea } from "@/components/ui";
import { Loader2 } from "lucide-react";

export default function SymptomCheckerApp() {
  const [symptoms, setSymptoms] = useState('');
  const [loading, setLoading] = useState(false);
  const [treatmentAdvice, setTreatmentAdvice] = useState('');

  const handleCheckSymptoms = async () => {
    if (!symptoms.trim()) {
      alert('Please enter your symptoms.');
      return;
    }

    setLoading(true);
    setTreatmentAdvice('');

    try {
      const response = await fakeAPICall(symptoms);
      setTreatmentAdvice(response);
    } catch (error) {
      console.error('Error fetching advice:', error);
      setTreatmentAdvice('Error fetching advice. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const fakeAPICall = (input) => {
    return new Promise((resolve, reject) => {
      if (!input) {
        reject('Invalid input for API call.');
      }
      setTimeout(() => {
        resolve(`Based on your symptoms: ${input}, it is recommended to rest, stay hydrated, and consult a doctor if symptoms persist.`);
      }, 2000);
    });
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <Card className="w-full max-w-lg p-4">
        <CardContent>
          <h1 className="text-2xl font-bold mb-4">AI Symptom Checker & Treatment Advisor</h1>
          <Textarea
            value={symptoms}
            onChange={(e) => setSymptoms(e.target.value)}
            placeholder="Enter your symptoms here..."
            className="w-full p-2 rounded border mb-4"
            rows={4}
          />
          <Button onClick={handleCheckSymptoms} className="w-full" disabled={loading}>
            {loading ? <Loader2 className="animate-spin mr-2" /> : 'Get Treatment Advice'}
          </Button>
          {treatmentAdvice && (
            <div className="mt-4 p-4 bg-blue-50 text-blue-900 rounded">
              <h2 className="text-lg font-semibold">Treatment Advice</h2>
              <p>{treatmentAdvice}</p>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
